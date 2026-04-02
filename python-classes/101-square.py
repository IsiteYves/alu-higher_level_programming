#!/usr/bin/python3
"""Defines a square."""


class Square:
    """Square class with __str__."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get size."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get pos."""
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Area."""
        return self.__size ** 2

    def __str__(self):
        """String rep."""
        if self.__size == 0:
            return ""
        res = []
        [res.append("") for i in range(self.__position[1])]
        for i in range(self.__size):
            res.append(" " * self.__position[0] + "#" * self.__size)
        return "\n".join(res)

    def my_print(self):
        """Print square."""
        print(self.__str__())
