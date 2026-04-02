#!/usr/bin/python3
"""Defines a square."""


class Square:
    """Square class with comparisons."""

    def __init__(self, size=0):
        """Initialize."""
        self.size = size

    @property
    def size(self):
        """Get size."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Area."""
        return self.__size ** 2

    def __eq__(self, o):
        """Equal."""
        return self.area() == o.area()

    def __ne__(self, o):
        """Not equal."""
        return self.area() != o.area()

    def __lt__(self, o):
        """Less."""
        return self.area() < o.area()

    def __le__(self, o):
        """Less equal."""
        return self.area() <= o.area()

    def __gt__(self, o):
        """Greater."""
        return self.area() > o.area()

    def __ge__(self, o):
        """Greater equal."""
        return self.area() >= o.area()
