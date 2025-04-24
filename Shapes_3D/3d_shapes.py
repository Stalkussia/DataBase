import math
import random
import math
import abc


class Shape3d(abc.ABC):
    @abc.abstractmethod
    def surface_area(self):
        pass
    @abc.abstractmethod
    def volume(self):
        pass

class Sphere(Shape3d):
    def __init__(self,radius):
        self.radius = radius
    def surface_area(self):
        return 4 * math.pi * self.radius ** 2
    def volume(self):
        return (4/3) * math.pi * self.radius ** 3

class Cylinder(Shape3d):
    def __init__(self,radius,height):
        self.radius = radius
        self.height = height
    def surface_area(self):
        return 2 * math.pi * self.radius * (self.radius + self.height)
    def volume(self):
        return math.pi * (self.radius ** 2) * self.height

class Cube(Shape3d):
    def __init__(self,length):
        self.length = length

    def surface_area(self):
        return 6 * (self.length ** 2)
    def volume(self):
        return self.length ** 3

shapes_list = []
for i in range(10):
    shape = random.choice(['Sphere','Cylinder','Cube'])
    if shape == 'Sphere':
        radius = (random.randint(1,10))
        shapes_list.append(Sphere(radius))
    elif shape == 'Cylinder':
        radius = random.randint(1,10)
        height = random.randint(5,20)
        shapes_list.append(Cylinder(radius,height))
    elif shape == 'Cube':
        length = random.randint(1,10)
        shapes_list.append(Cube(length))

for shape in shapes_list:
    shape_name = shape.__class__.__name__
    print(f"{shape_name}, {round(shape.surface_area(),2)}, {round(shape.volume(),2)}")


