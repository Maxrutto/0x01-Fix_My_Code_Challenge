#!/usr/bin/python3
"""
This class defines a square with its attributes
"""
class square():
    
    width = 0
    height = 0

    
    def __init__(self, *args, **kwargs):
        """ This instantiates the square object with attributes
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """ Method that finds the square perimeter
        """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ This prints a string representation of the object
        """
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":

    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
