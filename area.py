"""
Programmer: Boris Sodji
Date: 04AUG23
"""
# Importing math module to use pi and pow()
import math as m


def circle(radius):
    """
    Function that compute the area of a circle
    :param radius: radius of the circle
    :return: the area of the circle or raise a TypeError if the radius of the circle is less than 0
    """
    radius = float(radius)
    if radius <= 0:
        raise TypeError
    return m.pi * m.pow(radius, 2)

def square(side):
    """
    Function that compute the area of a square
    :param side: lenght of the square side
    :return: the area of the square or raise a TypeError if the side is less than 0
    """
    side = float(side)
    if side <= 0:
        raise TypeError
    return side ** 2


def rectangle(width, length):
    """
    Function that compute the area of a rectangle
    :param width: the width of the rectangle
    :param length: the lemght of the rectangle
    :return: the area of the rectangle or raise a TypeError if either the lenght or the width of the rectangle is less than 0
    """
    width = float(width)
    length = float(length)
    if width <= 0 or length <= 0:
        raise TypeError
    return width * length


def triangle(base, height):
    """
    Function that compute the area of a triangle
    :param base: the lenght of the base of the triangle
    :param height: the height of the triangle
    :return: the area of the triangle or raise a TypeError if either the base or the lenght of the triangle is less than 0
    """
    base = float(base)
    height = float(height)
    if base <= 0 or height <= 0:
        raise TypeError
    # Calculates the area of a triangle with the given base and height.
    return (base * height) / 2
