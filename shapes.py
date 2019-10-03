import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Point(x: %g, y: %g)" % (self.x, self.y)

class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x 
        self.y = y
        self.width = width
        self.height = height

    def rect_in_circle(self, circle):
        if not isinstance(circle, Circle):
            raise TypeError("The circle provided needs to be of type Circle!")
        points = (Point(self.x, self.y), Point(self.x + self.width, self.y), Point(self.x, self.y + self.height), Point(self.x + self.width, self.y + self.height))
        
        in_circle = True
        for point in points:
            in_circle &= circle.point_in_circle(point)
        return in_circle

class Circle:
    def __init__(self, center, radius):
        if not isinstance(center, Point):
            raise TypeError("Center is not a point!")
        if not isinstance(radius, (int, float)):
            raise TypeError("Radius is not a number!")
        self.center = center
        self.radius = radius

    def __str__(self):
        return "Circle(center: %s, radius: %g)" % (self.center, self.radius)

    def point_in_circle(self, point):
        if not isinstance(point, Point):
            raise TypeError("Point is not of type point!")
        distance = math.sqrt((point.x - self.center.x)**2 + (point.y - self.center.y)**2)
        return distance <= self.radius

if __name__ == "__main__":
    circle = Circle(Point(20, 20), 100)
    rect = Rectangle(20, 20, 10, 10)

    print(circle)

    print(rect.rect_in_circle(circle))
