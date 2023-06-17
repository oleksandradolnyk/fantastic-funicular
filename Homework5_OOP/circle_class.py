class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def contains(self, other):
        distance = (other.x - self.x)**2 + (other.y - self.y)**2
        if distance <= self.radius**2:
            return True
        else:
            return False


point = Point(2, 2)
circle = Circle(0, 0, 3)
print(circle.contains(point))
