import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circle:
    def __init__(self, center, radius):
        if not isinstance(center, Point):
            raise TypeError("Center is not a point!")
        if not isinstance(radius, (int, float)):
            raise TypeError("Radius is not a number!")
        self.center = center
        self.radius = radius

    def point_in_circle(self, point):
        if not isinstance(point, Point):
            raise TypeError("Point is not of type point!")
        distance = math.sqrt((point.x - self.center.x)**2 + (point.y - self.center.y)**2)
        return distance <= self.radius

circle = Circle(Point(20, 20), 100)
print(circle.point_in_circle(Point(119, 20)))
