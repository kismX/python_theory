# Create a base class called Shape with the following attributes and methods:
# Attributes:
# name (string)
# Methods:
# __init__(self, name): Initializes the name attribute.
# area(self): Computes and returns the area of the shape (0 by default).
# Create two subclasses, Rectangle and Circle, which inherit from the Shape class. 
# Each subclass should override the area method to compute the area specific to the shape.
# Additionally, create a function called total_area that takes a list of shapes and calculates the total area of all the shapes in the list.
# Finally, create instances of the Rectangle and Circle classes, add them to a list, 
# and use the total_area function to calculate and print the total area of all the shapes.


import math

class Shape:

    list_res = []
    
    def __init__(self, name: str):
        self.name = name
        self.result = 0

    def area(self, area=0):
        return area
    
    @classmethod
    def totalarea(cls):
        return sum(cls.list_res)
    
class Rectangle(Shape):
    
    def area(self, a, b):
        self.result = a * b
        self.list_res.append(self.result)
        return self.result

class Circle(Shape):
    
    def area(self, r):
        self.result = math.pi * (r ** 2)
        self.list_res.append(self.result)
        return self.result
    

rec = Rectangle("Rechteck")
shape = Shape("Scheißdreck")
circ = Circle("pepe")
print(rec.area(8, 2))
print(rec.area(8, 5))
print(circ.area(8))
print(shape.totalarea())