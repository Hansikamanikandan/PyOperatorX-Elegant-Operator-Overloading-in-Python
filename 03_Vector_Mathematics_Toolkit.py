class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar, self.z * scalar)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        return Vector(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

v1 = Vector(*map(int, input("Enter first vector (x y z): ").split()))
v2 = Vector(*map(int, input("Enter second vector (x y z): ").split()))
s = int(input("Enter scalar value: "))

print("Addition:", v1 + v2)
print("Subtraction:", v1 - v2)
print("Scalar Multiplication:", v1 * s)
print("Equal:", v1 == v2)
print("Dot Product:", v1.dot(v2))
print("Cross Product:", v1.cross(v2))
