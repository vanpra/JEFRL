"""
This type stub file was generated by pyright.
"""

from .objects import Object

class Value:
    def __init__(self, value) -> None:
        ...
    


class Params:
    def __init__(self, simple=..., message=..., stricted=..., firstRestricted=..., inFor=..., paramSet=..., params=..., get=...) -> None:
        ...
    


class Config(Object):
    def __init__(self, range=..., loc=..., source=..., tokens=..., comment=..., tolerant=..., **options) -> None:
        ...
    


class Context:
    def __init__(self, isModule=..., allowAwait=..., allowIn=..., allowStrictDirective=..., allowYield=..., firstCoverInitializedNameError=..., isAssignmentTarget=..., isBindingElement=..., inFunctionBody=..., inIteration=..., inSwitch=..., labelSet=..., strict=...) -> None:
        ...
    


class Marker:
    def __init__(self, index=..., line=..., column=...) -> None:
        ...
    


class TokenEntry(Object):
    def __init__(self, type=..., value=..., regex=..., range=..., loc=...) -> None:
        ...
    


class Parser:
    def __init__(self, code, options=..., delegate=...) -> None:
        ...
    
    def throwError(self, messageFormat, *args):
        ...
    
    def tolerateError(self, messageFormat, *args): # -> None:
        ...
    
    def unexpectedTokenError(self, token=..., message=...): # -> Error:
        ...
    
    def throwUnexpectedToken(self, token=..., message=...):
        ...
    
    def tolerateUnexpectedToken(self, token=..., message=...): # -> None:
        ...
    
    def collectComments(self): # -> None:
        ...
    
    def getTokenRaw(self, token):
        ...
    
    def convertToken(self, token): # -> TokenEntry:
        ...
    
    def nextToken(self): # -> RawToken:
        ...
    
    def nextRegexToken(self): # -> RawToken:
        ...
    
    def createNode(self): # -> Marker:
        ...
    
    def startNode(self, token, lastLineStart=...): # -> Marker:
        ...
    
    def finalize(self, marker, node):
        ...
    
    def expect(self, value): # -> None:
        ...
    
    def expectCommaSeparator(self): # -> None:
        ...
    
    def expectKeyword(self, keyword): # -> None:
        ...
    
    def match(self, *value): # -> bool:
        ...
    
    def matchKeyword(self, *keyword): # -> bool:
        ...
    
    def matchContextualKeyword(self, *keyword): # -> bool:
        ...
    
    def matchAssign(self): # -> bool:
        ...
    
    def isolateCoverGrammar(self, parseFunction):
        ...
    
    def inheritCoverGrammar(self, parseFunction):
        ...
    
    def consumeSemicolon(self): # -> None:
        ...
    
    def parsePrimaryExpression(self): # -> AsyncFunctionExpression | FunctionExpression | Identifier | Literal | TemplateLiteral | ArrowParameterPlaceHolder | SequenceExpression | ArrayExpression | ObjectExpression | RegexLiteral | ThisExpression | ClassExpression | Import:
        ...
    
    def parseSpreadElement(self):
        ...
    
    def parseArrayInitializer(self): # -> ArrayExpression:
        ...
    
    def parsePropertyMethod(self, params): # -> BlockStatement:
        ...
    
    def parsePropertyMethodFunction(self): # -> FunctionExpression:
        ...
    
    def parsePropertyMethodAsyncFunction(self): # -> AsyncFunctionExpression:
        ...
    
    def parseObjectPropertyKey(self): # -> Literal | Identifier | YieldExpression | AsyncArrowFunctionExpression | ArrowFunctionExpression | AsyncArrowParameterPlaceHolder | ConditionalExpression | BinaryExpression | UnaryExpression | AssignmentExpression | None:
        ...
    
    def isPropertyKey(self, key, value): # -> Literal[False]:
        ...
    
    def parseObjectProperty(self, hasProto):
        ...
    
    def parseObjectInitializer(self): # -> ObjectExpression:
        ...
    
    def parseTemplateHead(self): # -> TemplateElement:
        ...
    
    def parseTemplateElement(self): # -> TemplateElement:
        ...
    
    def parseTemplateLiteral(self): # -> TemplateLiteral:
        ...
    
    def reinterpretExpressionAsPattern(self, expr): # -> None:
        ...
    
    def parseGroupExpression(self): # -> ArrowParameterPlaceHolder | SequenceExpression:
        ...
    
    def parseArguments(self): # -> list[Unknown]:
        ...
    
    def isIdentifierName(self, token): # -> bool:
        ...
    
    def parseIdentifierName(self): # -> Identifier:
        ...
    
    def parseNewExpression(self): # -> MetaProperty | NewExpression:
        ...
    
    def parseAsyncArgument(self): # -> YieldExpression | AsyncArrowFunctionExpression | ArrowFunctionExpression | AsyncArrowParameterPlaceHolder | ConditionalExpression | BinaryExpression | UnaryExpression | AssignmentExpression | None:
        ...
    
    def parseAsyncArguments(self): # -> list[Unknown]:
        ...
    
    def matchImportCall(self): # -> Literal[False]:
        ...
    
    def parseImportCall(self): # -> Import:
        ...
    
    def parseLeftHandSideExpressionAllowCall(self): # -> Super | MetaProperty | NewExpression | StaticMemberExpression | AsyncArrowParameterPlaceHolder | CallExpression | ComputedMemberExpression | TaggedTemplateExpression:
        ...
    
    def parseSuper(self): # -> Super:
        ...
    
    def parseLeftHandSideExpression(self):
        ...
    
    def parseUpdateExpression(self):
        ...
    
    def parseAwaitExpression(self):
        ...
    
    def parseUnaryExpression(self): # -> UnaryExpression:
        ...
    
    def parseExponentiationExpression(self): # -> BinaryExpression | UnaryExpression:
        ...
    
    def binaryPrecedence(self, token): # -> int:
        ...
    
    def parseBinaryExpression(self): # -> BinaryExpression | UnaryExpression | None:
        ...
    
    def parseConditionalExpression(self): # -> ConditionalExpression | BinaryExpression | UnaryExpression | None:
        ...
    
    def checkPatternParam(self, options, param): # -> None:
        ...
    
    def reinterpretAsCoverFormalsList(self, expr): # -> Params | None:
        ...
    
    def parseAssignmentExpression(self): # -> YieldExpression | AsyncArrowFunctionExpression | ArrowFunctionExpression | AsyncArrowParameterPlaceHolder | ConditionalExpression | BinaryExpression | UnaryExpression | AssignmentExpression | None:
        ...
    
    def parseExpression(self): # -> SequenceExpression | YieldExpression | AsyncArrowFunctionExpression | ArrowFunctionExpression | AsyncArrowParameterPlaceHolder | ConditionalExpression | BinaryExpression | UnaryExpression | AssignmentExpression | None:
        ...
    
    def parseStatementListItem(self): # -> ExportDefaultDeclaration | ExportAllDeclaration | ExportNamedDeclaration | ExpressionStatement | ImportDeclaration | VariableDeclaration | AsyncFunctionDeclaration | FunctionDeclaration | ClassDeclaration | BlockStatement | EmptyStatement | LabeledStatement | BreakStatement | ContinueStatement | DebuggerStatement | DoWhileStatement | ForStatement | ForInStatement | ForOfStatement | IfStatement | ReturnStatement | SwitchStatement | ThrowStatement | TryStatement | WhileStatement | WithStatement:
        ...
    
    def parseBlock(self): # -> BlockStatement:
        ...
    
    def parseLexicalBinding(self, kind, options): # -> VariableDeclarator:
        ...
    
    def parseBindingList(self, kind, options): # -> list[Unknown | VariableDeclarator]:
        ...
    
    def isLexicalDeclaration(self): # -> bool:
        ...
    
    def parseLexicalDeclaration(self, options): # -> VariableDeclaration:
        ...
    
    def parseBindingRestElement(self, params, kind=...): # -> RestElement:
        ...
    
    def parseArrayPattern(self, params, kind=...):
        ...
    
    def parsePropertyPattern(self, params, kind=...): # -> Property:
        ...
    
    def parseRestProperty(self, params, kind): # -> RestElement:
        ...
    
    def parseObjectPattern(self, params, kind=...):
        ...
    
    def parsePattern(self, params, kind=...): # -> Identifier:
        ...
    
    def parsePatternWithDefault(self, params, kind=...): # -> AssignmentPattern | Identifier:
        ...
    
    def parseVariableIdentifier(self, kind=...): # -> Identifier:
        ...
    
    def parseVariableDeclaration(self, options): # -> VariableDeclarator:
        ...
    
    def parseVariableDeclarationList(self, options): # -> list[Unknown]:
        ...
    
    def parseVariableStatement(self): # -> VariableDeclaration:
        ...
    
    def parseEmptyStatement(self): # -> EmptyStatement:
        ...
    
    def parseExpressionStatement(self): # -> ExpressionStatement:
        ...
    
    def parseIfClause(self):
        ...
    
    def parseIfStatement(self): # -> IfStatement:
        ...
    
    def parseDoWhileStatement(self): # -> DoWhileStatement:
        ...
    
    def parseWhileStatement(self): # -> WhileStatement:
        ...
    
    def parseForStatement(self): # -> ForStatement | ForInStatement | ForOfStatement:
        ...
    
    def parseContinueStatement(self): # -> ContinueStatement:
        ...
    
    def parseBreakStatement(self): # -> BreakStatement:
        ...
    
    def parseReturnStatement(self): # -> ReturnStatement:
        ...
    
    def parseWithStatement(self): # -> WithStatement:
        ...
    
    def parseSwitchCase(self): # -> SwitchCase:
        ...
    
    def parseSwitchStatement(self): # -> SwitchStatement:
        ...
    
    def parseLabelledStatement(self): # -> LabeledStatement | ExpressionStatement:
        ...
    
    def parseThrowStatement(self): # -> ThrowStatement:
        ...
    
    def parseCatchClause(self): # -> CatchClause:
        ...
    
    def parseFinallyClause(self): # -> BlockStatement:
        ...
    
    def parseTryStatement(self): # -> TryStatement:
        ...
    
    def parseDebuggerStatement(self): # -> DebuggerStatement:
        ...
    
    def parseStatement(self): # -> ExpressionStatement | BlockStatement | EmptyStatement | AsyncFunctionDeclaration | FunctionDeclaration | LabeledStatement | BreakStatement | ContinueStatement | DebuggerStatement | DoWhileStatement | ForStatement | ForInStatement | ForOfStatement | IfStatement | ReturnStatement | SwitchStatement | ThrowStatement | TryStatement | VariableDeclaration | WhileStatement | WithStatement:
        ...
    
    def parseFunctionSourceElements(self): # -> BlockStatement:
        ...
    
    def validateParam(self, options, param, name): # -> None:
        ...
    
    def parseRestElement(self, params):
        ...
    
    def parseFormalParameter(self, options): # -> None:
        ...
    
    def parseFormalParameters(self, firstRestricted=...): # -> Params:
        ...
    
    def matchAsyncFunction(self): # -> Literal[False]:
        ...
    
    def parseFunctionDeclaration(self, identifierIsOptional=...): # -> AsyncFunctionDeclaration | FunctionDeclaration:
        ...
    
    def parseFunctionExpression(self): # -> AsyncFunctionExpression | FunctionExpression:
        ...
    
    def parseDirective(self): # -> Directive | ExpressionStatement:
        ...
    
    def parseDirectivePrologues(self): # -> list[Unknown]:
        ...
    
    def qualifiedPropertyName(self, token): # -> bool:
        ...
    
    def parseGetterMethod(self): # -> FunctionExpression:
        ...
    
    def parseSetterMethod(self): # -> FunctionExpression:
        ...
    
    def parseGeneratorMethod(self): # -> FunctionExpression:
        ...
    
    def isStartOfExpression(self): # -> bool:
        ...
    
    def parseYieldExpression(self): # -> YieldExpression:
        ...
    
    def parseClassElement(self, hasConstructor):
        ...
    
    def parseClassElementList(self): # -> list[Unknown]:
        ...
    
    def parseClassBody(self): # -> ClassBody:
        ...
    
    def parseClassDeclaration(self, identifierIsOptional=...): # -> ClassDeclaration:
        ...
    
    def parseClassExpression(self): # -> ClassExpression:
        ...
    
    def parseModule(self): # -> Module:
        ...
    
    def parseScript(self): # -> Script:
        ...
    
    def parseModuleSpecifier(self): # -> Literal:
        ...
    
    def parseImportSpecifier(self): # -> ImportSpecifier:
        ...
    
    def parseNamedImports(self): # -> list[Unknown]:
        ...
    
    def parseImportDefaultSpecifier(self): # -> ImportDefaultSpecifier:
        ...
    
    def parseImportNamespaceSpecifier(self): # -> ImportNamespaceSpecifier:
        ...
    
    def parseImportDeclaration(self): # -> ImportDeclaration:
        ...
    
    def parseExportSpecifier(self): # -> ExportSpecifier:
        ...
    
    def parseExportDefaultSpecifier(self): # -> ExportDefaultSpecifier:
        ...
    
    def parseExportDeclaration(self): # -> ExportDefaultDeclaration | ExportAllDeclaration | ExportNamedDeclaration:
        ...
    


