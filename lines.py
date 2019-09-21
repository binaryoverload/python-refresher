from vectors import (Vector2, Vector3)

class Line:

    def __init__(self, start, end):
        if not (isinstance(start, (Vector2, Vector3)) and isinstance(end, (Vector2, Vector3)) and type(start) == type(end)):
            raise TypeError("Both the start and end points of the line need to be a Vector2 or Vector3 (Start and end need to match type)")
        self.start = start
        self.end = end

    def length(self):
        return (self.end - self.start).magnitude()

print(Line(Vector2(0, 0), Vector2(3, 4)).length())