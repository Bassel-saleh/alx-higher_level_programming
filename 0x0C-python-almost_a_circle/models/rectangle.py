#!/usr/bin/python3
''' Define class Rectangle '''
from models.base import Base


class Rectangle(Base):
    """ Represents Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        ''' constructor '''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        ''' represents width of rectangle '''
        return self. __width

    @width.setter
    def width(self, value):
        self.validateIfInteger("width", value, False)
        self.__width = value

    @property
    def height(self):
        ''' represents height of rectangle '''
        return self.__height

    @height.setter
    def height(self, value):
        self.validateIfInteger("height", value, False)
        self.__height = value

    @property
    def x(self):
        ''' represents x of rectangle '''
        return self.__x

    @x.setter
    def x(self, value):
        self.validateIfInteger("x", value)
        self.__x = value

    @property
    def y(self):
        ''' represents y of rectangle '''
        return self.__y

    @y.setter
    def y(self, value):
        self.validateIfInteger("y", value)
        self.__y = value

    def validateIfInteger(self, name, value, eq=True):
        ''' basicly isint function '''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        '''returns area of rectangle '''
        return self.width * self.height

    def display(self):
        ''' display rectangle using '#' '''
        s = '\n' * self.y + \
            (' ' * self.x + '#' * self.width + '\n') * self.height
        print(s, end='')

    def __str__(self):
        ''' returns str info about rectangle '''
        return '[{}] ({}) {}/{} - {}/{}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width,
                   self.height)

    def updateHelper(self, id=None, width=None, height=None, x=None, y=None):
        ''' update function helper '''
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        ''' it updates the values of a rectangle '''
        # print(args, kwargs)
        if args:
            self.updateHelper(*args)
        elif kwargs:
            self.updateHelper(**kwargs)
