import math


class Shape:

    def square(self):
        return 0


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def square(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def square(self):
        return self.width * self.height


class Parallelogram(Rectangle):

    def __init__(self, height, width, angle):
        super().__init__(height, width)
        self.angle = angle
        self.base = width

    def print_angle(self):
        print(self.angle)

    def __str__(self):
        result = super().__str__()
        return result + f'\nParallelogram: {self.width}, {self.height}, {self.angle}'

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def square(self):
        return self.base * self.height


class Triangle(Rectangle):
    def square(self):
        return (self.width * self.height) / 2


class Scene:
    def __init__(self):
        self._figures = []

    def add_figure(self, figure):
        self._figures.append(figure)

    def total_square(self):
        return sum(f.square() for f in self._figures)

    def __str__(self):
        pass


r = Rectangle(10, 20)
r1 = Rectangle(-10, 20)
r2 = Rectangle(100, 20)

c = Circle(10)
c1 = Circle(5)

p = Parallelogram(20, 30, 45)
p1 = Parallelogram(10, 15, 20)

t = Triangle(10, 5)
t2 = Triangle(5, 5)

figures = [r, r1, r2, c, c1, p, p1, t, t2]

scene = Scene()

for figure in figures:
    scene.add_figure(figure)

print(scene.total_square())
