import copy
import random
import re

from torch import rand

from js_ast.nodes import Identifier, Literal, Node
from js_ast.scope import Scope, ScopeType
from utils.interesting_values import interesting_floats, interesting_integers


# Calculates variables, classes and functions available at each node and stores it in
# a node attribute
def scope_analysis(node: Node, scope: Scope = Scope()):
    if node.type == "Identifier" or node.type == "Literal":
        return

    node.scope = copy.deepcopy(scope)

    if (
        node.type == "Program"
        or node.type == "BlockStatement"
        or node.type == "ClassBody"
    ):
        if node.type == "ClassBody":
            new_scope = Scope(parent=scope, scope_type=ScopeType.CLASS)
        elif (
            node.type == "BlockStatement" and node.parent.type == "FunctionDeclaration"
        ):
            new_scope = Scope(parent=scope, scope_type=ScopeType.FUNCTION)
        else:
            new_scope = Scope(parent=scope, scope_type=ScopeType.BLOCK)

        functions = filter(lambda x: x.type == "FunctionDeclaration", node.body)
        classes = filter(lambda x: x.type == "ClassDeclaration", node.body)
        methods = filter(
            lambda x: x.type == "MethodDefinition" and x.kind != "constructor",
            node.body,
        )

        for function in functions:
            new_scope.functions[function.id.name] = function.params
        for class_ in classes:
            new_scope.classes.add(class_.id.name)
        for method in methods:
            new_scope.functions[method.key.name] = method.value.params

        for item in node.body:
            scope_analysis(item, new_scope)

        # Store the scope at the end of the block so that it can be used for add mutation
        node.end_scope = copy.deepcopy(new_scope)

    elif node.type == "VariableDeclarator":
        if node.init:
            scope_analysis(node.init, scope)
        if node.kind == "var":
            current_scope = scope
            while current_scope.parent and current_scope.scope_type != ScopeType.BLOCK:
                current_scope = current_scope.parent

            current_scope.variables.add(node.id.name)
            scope.parent_variables.add(node.id.name)
        else:
            scope.variables.add(node.id.name)
    else:
        for child in node.children():
            scope_analysis(child, scope)


# Fixes the node by replacing identifiers and function calls with available variables and
# functions
def fix_node_references(node: Node):
    scope = node.scope
    if node.type == "Identifier":
        if scope.available_variables() and node.name not in scope.available_variables():
            node.name = random.choice(list(scope.available_variables()))

    elif node.type == "CallExpression":
        if node.callee.type == "Identifier":
            if (
                scope.available_functions()
                and node.callee.name not in scope.available_functions()
            ):
                function, params = random.choice(
                    list(scope.available_functions().items())
                )
                node.callee.name = function
                node.arguments = [random_value(scope, node) for _ in range(len(params))]
    else:
        for child in node.children():
            fix_node_references(child)


# Gets random literal or identifier
def random_value(scope: Scope, parent: Node):
    if scope.available_variables() and random.random() < 0.5:
        return Identifier(
            name=random.choice(list(scope.available_variables())), parent=parent
        )
    else:
        # TODO: add more types and interesting values
        if random.random() < 0.5:
            value = random.choice(interesting_integers)
        else:
            value = random.choice(interesting_floats)

        return Literal(
            value=value,
            raw=str(value),
            parent=parent,
        )
