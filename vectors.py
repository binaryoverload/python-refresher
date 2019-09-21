import math

class Vector2:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Vector2(x: %g, y: %g)" % (self.x, self.y)

    def __add__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x + other.x, self.y + other.y)
        elif isinstance(other, (int, float)):
            return Vector2(self.x + other, self.y + other)
        else: 
            raise TypeError("You can only add a Vector2 or scalar onto a Vector2!")

    def __sub__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x - other.x, self.y - other.y)
        elif isinstance(other, (int, float)):
            return Vector2(self.x - other, self.y - other)
        else:
            raise TypeError("You can only subtract a Vector2 or scalar from a Vector2!")

    def __mul__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError("Vectors can only be multiplied by a scalar value!")
        return Vector2(self.x * other, self.y * other)

    def magnitude(self):
        return math.sqrt((self.x)**2 + (self.y)**2)

    def normalise(self):
        return Vector2(self.x / self.magnitude(), self.y / self.magnitude())

class Vector3:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "Vector3(x: %g, y: %g, z: %g)" % (self.x, self.y, self.z)

    def __add__(self, other):
        if isinstance(other, Vector3):
            return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
        elif isinstance(other, (int, float)):
            return Vector3(self.x + other, self.y + other, self.z + other)
        else: 
            raise TypeError("You can only add a Vector3 or scalar onto a Vector3!")

    def __sub__(self, other):
        if isinstance(other, Vector3):
            return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
        elif isinstance(other, (int, float)):
            return Vector3(self.x - other, self.y - other, self.z - other)
        else:
            raise TypeError("You can only subtract a Vector3 or scalar from a Vector3!")

    def __mul__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError("Vectors can only be multiplied by a scalar value!")
        return Vector3(self.x * other, self.y * other, self.z * other)

    def magnitude(self):
        return math.sqrt((self.x)**2 + (self.y)**2 + (self.z)**2)

    def normalise(self):
        return Vector3(self.x / self.magnitude(), self.y / self.magnitude(), self.z / self.magnitude())


        