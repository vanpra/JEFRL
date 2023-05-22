from __future__ import annotations

from abc import ABC, abstractmethod
import ctypes
from enum import StrEnum
import math
from multiprocessing import shared_memory
import os
from pathlib import Path
import subprocess
import tempfile
from typing import Any, Optional

import numpy as np
from numpy.typing import NDArray


SHM_SIZE = 0x100000
MAX_EDGES = (SHM_SIZE - 4) * 8
SHM_ID = "js_rl"

ENGINES_DIR = Path("engines")
CORPUS_DIR = Path("corpus")


class JSError(StrEnum):
    ReferenceError = "ReferenceError"
    SyntaxError = "SyntaxError"
    TypeError = "TypeError"
    Other = "Other"
    TimeoutError = "TimeoutError"
    NoError = "NoError"


class ShmData(ctypes.Structure):
    _fields_ = [
        ("num_edges", ctypes.c_uint32),
        ("edges", ctypes.c_ubyte * (SHM_SIZE - 4)),
    ]


class CoverageData:
    def __init__(self, num_edges: int = 0, edges: Optional[NDArray[np.ubyte]] = None):
        self.num_edges = num_edges
        self.edges = (
            np.zeros(math.ceil(self.num_edges / 8), dtype=np.ubyte)
            if edges is None
            else edges
        )
        self.hit_edges: int = np.unpackbits(self.edges).sum()  # type: ignore

    def coverage(self) -> float:
        return self.hit_edges / self.num_edges if self.num_edges > 0 else 0

    def __or__(self, __value: Any) -> CoverageData:
        if not isinstance(__value, CoverageData):
            raise TypeError(
                "Cannot perform bitwise or on CoverageData and " + type(__value)
            )
        if self.num_edges == __value.num_edges:
            return CoverageData(
                self.num_edges,
                self.edges | __value.edges,
            )
        elif self.num_edges == 0:
            return __value
        elif __value.num_edges == 0:
            return self

        raise ValueError("Cannot perform bitwise or on CoverageData with given objects")

    def __str__(self) -> str:
        return f"{self.coverage():.5%}"

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, CoverageData):
            return False

        return (
            self.edges == __value.edges
        ).all() and self.num_edges == __value.num_edges

    def __deepcopy__(self, memo: dict[int, Any]) -> CoverageData:
        return CoverageData(self.num_edges, self.edges.copy())


class ExecutionData:
    def __init__(self, coverage_data: CoverageData, error: JSError, out: str):
        self.error = error
        self.coverage_data = coverage_data
        self.out = out

    def is_crash(self):
        return self.error == JSError.Other


class Engine(ABC):
    def __init__(self) -> None:
        with open(self.corpus_lib_path, "r") as f:
            self.lib = f.read()

    @property
    @abstractmethod
    def executable(self) -> Path:
        pass

    @property
    @abstractmethod
    def args(self) -> list[str]:
        pass

    @property
    @abstractmethod
    def corpus_path(self) -> Path:
        pass

    @property
    @abstractmethod
    def corpus_lib_path(self) -> Path:
        pass

    def execute_text(self, code: str) -> Optional[ExecutionData]:
        tmp = tempfile.NamedTemporaryFile(delete=True)
        tmp.write(self.lib.encode("utf-8"))
        tmp.write(code.encode("utf-8"))
        tmp.flush()

        return self.execute_file(tmp.name)

    def execute_file(self, file: str):
        shm = shared_memory.SharedMemory(name=SHM_ID, create=True, size=SHM_SIZE)
        os.environ["SHM_ID"] = SHM_ID
        out: Optional[str] = None

        try:
            res = subprocess.run(
                [self.executable, *self.args, file],
                capture_output=True,
                check=False,
                timeout=5,
            )
            out = res.stdout.decode("utf-8")
            error = JSError.NoError
            if "ReferenceError" in out:
                error = JSError.ReferenceError
            elif "SyntaxError" in out:
                error = JSError.SyntaxError
            elif "TypeError" in out:
                error = JSError.TypeError
            elif res.returncode != 0:
                error = JSError.Other
        except subprocess.TimeoutExpired:
            error = JSError.TimeoutError

        data = ShmData.from_buffer(shm.buf)
        exec_data = ExecutionData(
            CoverageData(int(data.num_edges), np.array(data.edges, dtype=np.ubyte)),
            error,
            out if out is not None else "",
        )

        del data

        shm.close()
        shm.unlink()

        return exec_data


class V8Engine(Engine):
    @property
    def args(self) -> list[str]:
        return [
            "--expose-gc",
            "--omit-quit",
            "--allow-natives-syntax",
            "--fuzzing",
            # "--jit-fuzzing",
            "--future",
            "--harmony",
        ]

    @property
    def executable(self) -> Path:
        return ENGINES_DIR / "v8/v8/out/fuzzbuild/d8"

    @property
    def corpus_path(self) -> Path:
        return CORPUS_DIR / "v8-latest"

    @property
    def corpus_lib_path(self) -> Path:
        return CORPUS_DIR / "libs/v8.js"
