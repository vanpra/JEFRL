from __future__ import annotations

import ctypes
import math
import os
import subprocess
import sys
import tempfile
from abc import ABC, abstractmethod
from multiprocessing import shared_memory
from pathlib import Path
from typing import Any, Optional

from strenum import StrEnum

from js_ast import escodegen
from js_ast.nodes import Node

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
    NoError = "NoError"


class ShmData(ctypes.Structure):
    _fields_ = [
        ("num_edges", ctypes.c_uint32),
        ("edges", ctypes.c_ubyte * (SHM_SIZE - 4)),
    ]


class CoverageData:
    def __init__(self, num_edges: int = 0, edges: bytearray = bytearray()):
        self.num_edges = num_edges
        self.edges = edges
        self.hit_edges = 0

        for i in range(math.ceil(self.num_edges / 8)):
            self.hit_edges += self.edges[i].bit_count()

    def coverage(self):
        return self.hit_edges / self.num_edges if self.num_edges > 0 else 0

    def __or__(self, __value: Any) -> CoverageData:
        if not isinstance(__value, CoverageData):
            raise TypeError(
                "Cannot perform bitwise or on CoverageData and " + type(__value)
            )
        elif self.num_edges == 0 and __value.num_edges != 0:
            return __value
        elif self.num_edges != 0 and __value.num_edges == 0:
            return self
        elif self.num_edges != __value.num_edges:
            raise ValueError(
                "Cannot perform bitwise or on CoverageData with different number of edges"
            )

        return CoverageData(
            self.num_edges,
            bytearray([a | b for a, b in zip(self.edges, __value.edges)]),
        )

    def __str__(self) -> str:
        return f"CoverageData({self.coverage()})"

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, CoverageData):
            return False

        return self.edges == __value.edges and self.num_edges == __value.num_edges


class ExecutionData:
    def __init__(self, coverage_data: CoverageData, error: JSError, out: str):
        self.error = error
        self.coverage_data = coverage_data
        self.out = out

    def is_crash(self):
        return self.error == JSError.Other


class Engine(ABC):
    def __init__(self) -> None:
        with open(self.get_corpus_lib(), "r") as f:
            self.lib = f.read()

    @abstractmethod
    def get_executable(self) -> str:
        pass

    @abstractmethod
    def get_corpus(self) -> str:
        pass

    @abstractmethod
    def get_corpus_lib(self) -> str:
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

        res = subprocess.run(
            [self.get_executable(), file], capture_output=True, check=False
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

        data = ShmData.from_buffer(shm.buf)
        exec_data = ExecutionData(
            CoverageData(int(data.num_edges), bytearray(data.edges)), error, out
        )

        del data

        shm.close()
        shm.unlink()

        return exec_data


class V8Engine(Engine):
    def get_executable(self) -> Path:
        return ENGINES_DIR / "v8/v8/out/fuzzbuild/d8"

    def get_corpus(self) -> Path:
        return CORPUS_DIR / "v8"

    def get_corpus_lib(self) -> Path:
        return CORPUS_DIR / "libs/v8.js"
