#!/usr/bin/python3
''' defining Square class '''
from models.rectangle import Rectangle


class Square(Rectangle):
    ''' Square subclass '''

    def __init__(self, size, x=0, y=0, id=None):
        ''' constructor '''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        'returns str info of square '''
        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        ''' represents size of a rectangle '''
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def updateHelper(self, id=None, size=None, x=None, y=None):
        ''' update function helper '''
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        ''' it updates the values of a rectangle '''
        if args:
            self.updateHelper(*args)
        elif kwargs:
            self.updateHelper(**kwargs)

    def to_dictionary(self):
        ''' Returns dictionary of this class '''
        return {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}
