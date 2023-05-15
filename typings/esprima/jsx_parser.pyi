"""
This type stub file was generated by pyright.
"""

from .parser import Parser

class MetaJSXElement:
    def __init__(self, node=..., opening=..., closing=..., children=...) -> None:
        ...
    


class JSXToken:
    Identifier = ...
    Text = ...


class RawJSXToken:
    def __init__(self, type=..., value=..., lineNumber=..., lineStart=..., start=..., end=...) -> None:
        ...
    


def getQualifiedElementName(elementName):
    ...

class JSXParser(Parser):
    def __init__(self, code, options, delegate) -> None:
        ...
    
    def parsePrimaryExpression(self): # -> JSXElement | AsyncFunctionExpression | FunctionExpression | Identifier | Literal | TemplateLiteral | ArrowParameterPlaceHolder | SequenceExpression | ArrayExpression | ObjectExpression | RegexLiteral | ThisExpression | ClassExpression | Import:
        ...
    
    def startJSX(self): # -> None:
        ...
    
    def finishJSX(self): # -> None:
        ...
    
    def reenterJSX(self): # -> None:
        ...
    
    def createJSXNode(self): # -> Marker:
        ...
    
    def createJSXChildNode(self): # -> Marker:
        ...
    
    def scanXHTMLEntity(self, quote):
        ...
    
    def lexJSX(self): # -> RawJSXToken | RawToken:
        ...
    
    def nextJSXToken(self): # -> RawJSXToken | RawToken:
        ...
    
    def nextJSXText(self): # -> RawJSXToken:
        ...
    
    def peekJSXToken(self): # -> RawJSXToken | RawToken:
        ...
    
    def expectJSX(self, value): # -> None:
        ...
    
    def matchJSX(self, *value): # -> bool:
        ...
    
    def parseJSXIdentifier(self): # -> JSXIdentifier:
        ...
    
    def parseJSXElementName(self): # -> JSXNamespacedName | JSXIdentifier | JSXMemberExpression:
        ...
    
    def parseJSXAttributeName(self): # -> JSXNamespacedName | JSXIdentifier:
        ...
    
    def parseJSXStringLiteralAttribute(self): # -> Literal:
        ...
    
    def parseJSXExpressionAttribute(self): # -> JSXExpressionContainer:
        ...
    
    def parseJSXAttributeValue(self): # -> JSXExpressionContainer | JSXElement | Literal:
        ...
    
    def parseJSXNameValueAttribute(self): # -> JSXAttribute:
        ...
    
    def parseJSXSpreadAttribute(self): # -> JSXSpreadAttribute:
        ...
    
    def parseJSXAttributes(self): # -> list[Unknown]:
        ...
    
    def parseJSXOpeningElement(self): # -> JSXOpeningElement:
        ...
    
    def parseJSXBoundaryElement(self): # -> JSXClosingElement | JSXOpeningElement:
        ...
    
    def parseJSXEmptyExpression(self): # -> JSXEmptyExpression:
        ...
    
    def parseJSXExpressionContainer(self): # -> JSXExpressionContainer:
        ...
    
    def parseJSXChildren(self): # -> list[Unknown]:
        ...
    
    def parseComplexJSXElement(self, el): # -> MetaJSXElement:
        ...
    
    def parseJSXElement(self): # -> JSXElement:
        ...
    
    def parseJSXRoot(self): # -> JSXElement:
        ...
    
    def isStartOfExpression(self): # -> bool:
        ...
    


