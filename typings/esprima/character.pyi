"""
This type stub file was generated by pyright.
"""

U_CATEGORIES = ...
UNICODE_LETTER = ...
UNICODE_OTHER_ID_START = ...
UNICODE_OTHER_ID_CONTINUE = ...
UNICODE_COMBINING_MARK = ...
UNICODE_DIGIT = ...
UNICODE_CONNECTOR_PUNCTUATION = ...
IDENTIFIER_START = ...
IDENTIFIER_PART = ...
WHITE_SPACE = ...
LINE_TERMINATOR = ...
DECIMAL_CONV = ...
OCTAL_CONV = ...
HEX_CONV = ...
DECIMAL_DIGIT = ...
OCTAL_DIGIT = ...
HEX_DIGIT = ...
class Character:
    @staticmethod
    def fromCodePoint(code):
        ...
    
    @staticmethod
    def isWhiteSpace(ch): # -> bool:
        ...
    
    @staticmethod
    def isLineTerminator(ch): # -> bool:
        ...
    
    @staticmethod
    def isIdentifierStart(ch): # -> bool:
        ...
    
    @staticmethod
    def isIdentifierPart(ch): # -> bool:
        ...
    
    @staticmethod
    def isDecimalDigit(ch): # -> bool:
        ...
    
    @staticmethod
    def isHexDigit(ch): # -> bool:
        ...
    
    @staticmethod
    def isOctalDigit(ch): # -> bool:
        ...
    


