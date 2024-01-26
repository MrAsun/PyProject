#
import math
#
from PyProject import False_to_exception
from PyProject import Math







    # ========== Vector 2
class Vector2:
    
    # Initialization
    def __init__(self, x, y):
        # Attributes
        self.__x = x
        self.__y = y     
               
    # Return self
    def __call__(self):
        return (self.__x, self.__y)        


    # Getters and setters
        # Setters
    def set_x(self, x):
        if False_to_exception(type(x, int) or type(x, float), "Type error!!! This attribute can be only int or float!!!"):
            self.__x = x        
    def set_y(self, y):
        if False_to_exception(type(y, int) or type(y, float), "Type error!!! This attribute can be only int or float!!!"):
            self.__y = y  
        # Set attributes
    x = property(lambda self: self.__x, set_x)
    y = property(lambda self: self.__y, set_y)


    # Arithmetic
    def __add__(self, other):
        if type(other, Vector2):
            return Vector2(self.__x + other.__x, self.__y + other.__y)
        if type(other, int) or type(other, float):
            return Vector2(self.__x + other, self.__y + other)
    def __sub__(self, other):
        if type(other, Vector2):
            return Vector2(self.__x - other.__x, self.__y - other.__y)
        if type(other, int) or type(other, float):
            return Vector2(self.__x - other, self.__y - other)
    def __truediv__(self, other):
        if type(other, Vector2):
            return Vector2(self.__x / other.__x, self.__y / other.__y)
        if type(other, int) or type(other, float):
            return Vector2(self.__x / other, self.__y / other)
    def __mul__(self, other):
        if type(other, Vector2):
            return Vector2(self.__x * other.__x, self.__y * other.__y)
        if type(other, int) or type(other, float):
            return Vector2(self.__x * other, self.__y * other)



    # Addition
        # Distance
    @staticmethod
    def distance(pos1, pos2):
        return math.sqrt((pos2.x - pos1.x) ** 2 + (pos2.y- pos1.y) ** 2)
        # Axis
    @staticmethod
    def Up():
        return Vector2(0, 1)
    @staticmethod
    def Down():
        return Vector2(0, -1)
    @staticmethod
    def Right():
        return Vector2(1, 0)
    @staticmethod
    def Left():
        return Vector2(-1, 0)
        # Get direction
    @staticmethod
    def Direction(angle):
        return Vector2(Math.cos(angle), Math.sin(angle))









#   # ========== Color
class Color:
    
    # Initialization
    def __init__(self, red, blue, green):
        # Attributes
        self.__red = Math.clamp(red, 0, 255)
        self.__blue = Math.clamp(blue, 0, 255)
        self.__green = Math.clamp(green, 0, 255)
        
    # Return self
    def __call__(self):
        return (self.__red, self.__blue, self.__green)        



    # Getters and setter
        # Settters
    def set_red(self, red):
        if False_to_exception(type(red, int), "Type error!!! This attribute can be only int!!!"):
            self.__red = red
    def set_blue(self, blue):
        if False_to_exception(type(blue, int), "Type error!!! This attribute can be only int!!!"):
            self.__blue = blue
    def set_green(self, green):
        if False_to_exception(type(green, int), "Type error!!! This attribute can be only int!!!"):
            self.__green = green
        # Register attributes
    red = property(lambda self: self.__red, set_red)
    blue = property(lambda self: self.__blue, set_blue)
    green = property(lambda self: self.__green, set_green)