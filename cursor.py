"""Cursor"""
from character import IndexCursor


class Cursor:
    """move cursor"""
    def __init__(self, document):
        """
        :param document: Document
        >>> cursor = Cursor('a')
        >>> cursor.position
        0
        """
        self.document = document
        self.position = 0

    def forward(self):
        """
        move cursor forward
        """
        if self.position > len(self.document.characters) or self.position < 0:
            raise IndexCursor
        self.position += 1

    def back(self):
        """
        move cursor back
        """
        if self.position > len(self.document.characters) or self.position < 0:
            raise IndexCursor
        self.position -= 1

    def home(self):
        """
        move cursor to the beginning of the line
        """
        if self.position > len(self.document.characters) or self.position < 0:
            raise IndexCursor
        while self.document.characters[self.position - 1].character != '\n':
            self.position -= 1
            if self.position == 0: # Got to beginning of file before newline
                break

    def end(self):
        """
        move cursor to the end
        """
        if self.position > len(self.document.characters) or self.position < 0:
            raise IndexCursor
        while self.position < len(self.document.characters) and \
                self.document.characters[self.position].character != '\n':
            self.position += 1
