#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

my_square = Rectangle.square(5)
print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))
print(my_square)

my_square1 = Rectangle.square(3)
print("Area: {} - Perimeter: {}".format(my_square1.area(), my_square1.perimeter()))
print(my_square1)