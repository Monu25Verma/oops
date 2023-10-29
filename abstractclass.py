
from abc import ABCMeta, abstractmethod

class Shape(metaclass = ABCMeta):
    @abstractmethod
    def area(selmetf):
        return 0
    
class Square(Shape):
    side = 4
    def area( self):
        print("the area of square is: ", self.side * self.side)

class Rectangle(Shape):
    length = 5
    breadth = 10

    def area(self):
        print("the area of rectangle is ", self.length * self.breadth)


square = Square()
square.area()
rectangle = Rectangle()
rectangle.area()
square = Square()