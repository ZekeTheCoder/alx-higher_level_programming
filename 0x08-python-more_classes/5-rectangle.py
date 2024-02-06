#!/usr/bin/python3
"""
Write a class Rectangle that defines a rectangle by: (based on 4-rectangle.py)
- Print the message Bye rectangle...(... being 3 dots not ellipsis)
when an instance of Rectangle is deleted.
"""


class Rectangle:
    """ Class that defines a rectangle """

    def __init__(self, width=0, height=0):
        """ method that instantiates with optional width and height
        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ method that retrieves the width of the rectangle
        Returns:
            width of the rectangle
        """

        return self.__width

    @width.setter
    def width(self, value):
        """ method that sets the width of the rectangle
        Args:
            value: width
        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than zero
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ method that retrieves the height of the rectangle
        Returns:
            height of the rectangle
        """

        return self.__height

    @height.setter
    def height(self, value):
        """ method that sets the height of the rectangle
        Args:
            value: height
        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than zero
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Method that calculates the area of the rectangle
        Returns:
            area of the rectangle
        """
        return (self.width * self.height)

    def perimeter(self):
        """ Method that calculates the perimeter of the rectangle
        Returns:
            perimeter of the rectangle
        """
        if self.width == 0 or self.height == 0:
            return (0)
        return ((self.width * 2) + (self.height * 2))

    def __str__(self):
        """ String representation of the rectangle
        Returns:
            print the rectangle with the character #
        """

        rectangle = ""

        if self.width == 0 or self.height == 0:
            return rectangle

        for i in range(self.height):
            rectangle += ("#" * self.width) + "\n"

        return rectangle[:-1]

    def __repr__(self):
        """ This method recreate a new instance by using eval() """

        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Destructor method - defines instance method to delete rectangle"""

        print("Bye rectangle...")
