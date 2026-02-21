import copy
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def draw(self):
        return f"Drawing Square with side {self.side}"

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def draw(self):
        return f"Drawing circle with radius {self.radius}"

class Art:
    def __init__(self, color, shapes):
        self.color = color
        self.shapes = shapes
        
    def addToShapes(self, shape):
        self.shapes.append(shape)
    
    def draw(self):
        print(f"Background color {self.color}")
        [print(x.draw()) for x in self.shapes]

shapes = [Square(5), Square(3), Circle(10)]

a1 = Art("Red", shapes)
a2 = copy.copy(a1) # shallow copy
a3 = copy.deepcopy(a1)
a1.addToShapes(Circle(5)) # deep copy

a1.draw()
print("-------------")
a2.draw()
print("-------------")
a3.draw()


