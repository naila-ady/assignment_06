"""Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a
class Rectangle that implements area().

"""
from abc import ABC, abstractmethod

# Abstract Base Class
class Shape(ABC):
    @abstractmethod
    def area(self):## area() is defined as an abstract placeholder: it says "Every shape must have a way to 
        pass      # calculate area, but I won't define it here. so each shape should know"
    

# Concrete subclass implementing the abstract method
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Creating an object of Rectangle
rect = Rectangle(5, 3)
print(f"The area of the rectangle is: {rect.area()}")
