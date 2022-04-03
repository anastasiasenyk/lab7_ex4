"""Main"""
from cursor import Cursor
from character import Character, LenCharacter, IndexCursor


class Document:
    """str"""
    def __init__(self):
        """
        initial
        >>> d = Document()
        >>> d.characters
        []
        """
        self.characters = []
        self.cursor = Cursor(self)
        self.filename = ''

    def insert(self, character):
        """
        insert character in document
        >>> d = Document()
        >>> d.insert('a')
        >>> d.cursor.position
        1
        """
        try:
            if not hasattr(character, 'character'):
                    character = Character(character)

            self.characters.insert(self.cursor.position, character)
            self.cursor.forward()
        except LenCharacter:
            print('You only need to enter one item')
        except IndexCursor:
            print('wrong index of cursor')

    def delete(self):
        """
        insert character in document
        >>> d = Document()
        >>> d.insert('a')
        >>> d.cursor.back()
        >>> d.delete()
        >>> d.characters
        []
        """
        try:
            del self.characters[self.cursor.position]
        except IndexCursor:
            print('wrong index of cursor')

    def save(self):
        """save str to file"""
        try:
            f = open(self.filename, 'w')
            f.write(''.join(self.characters))
            f.close()
        except FileNotFoundError:
            print('no such file or directory')

    @property
    def string(self):
        """
        :return: str
        """
        return "".join((str(c) for c in self.characters))
