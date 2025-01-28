
from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    @abstractmethod
    def area(self):

        raise NotImplementedError("Subclass must implement area()")
    
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
      from math import pi
      return pi * self.radius ** 2
    
if __name__ == "__main__":
    circle = Circle(5)
    print(f"Area of the circle: {circle.area():.2f}")

