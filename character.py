"""Exceptions, Cursor"""


class DocException(Exception):
    """class of exception"""
    pass


class IndexCursor(DocException):
    """cursor has wrong index"""
    pass


class LenCharacter(DocException):
    """len(character) != 1"""
    pass


class Character:
    """Character"""
    def __init__(self, character, bold=False, italic=False, underline=False):
        """
        :param character: str
        :param bold: bool
        :param italic: bool
        :param underline: bool
        >>> ch = Character('a', True)
        >>> ch.character
        'a'
        """
        if len(character) != 1:
            raise LenCharacter()
        self.character = character
        self.bold = bold
        self.italic = italic
        self.underline = underline

    def __str__(self):
        """
        :return: str
        >>> print(Character('a', True))
        *a
        """
        bold = "*" if self.bold else ''
        italic = "/" if self.italic else ''
        underline = "_" if self.underline else ''
        return bold + italic + underline + self.character

