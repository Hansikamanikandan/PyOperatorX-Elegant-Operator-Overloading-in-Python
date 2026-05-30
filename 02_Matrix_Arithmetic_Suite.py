class Matrix:
    def __init__(self, data):
        self.data = data

    def __add__(self, other):
        return Matrix([[self.data[i][j] + other.data[i][j]
                        for j in range(len(self.data[0]))]
                       for i in range(len(self.data))])

    def __sub__(self, other):
        return Matrix([[self.data[i][j] - other.data[i][j]
                        for j in range(len(self.data[0]))]
                       for i in range(len(self.data))])

    def __mul__(self, other):
        result = [[0 for _ in range(len(other.data[0]))]
                  for _ in range(len(self.data))]
        for i in range(len(self.data)):
            for j in range(len(other.data[0])):
                for k in range(len(other.data)):
                    result[i][j] += self.data[i][k] * other.data[k][j]
        return Matrix(result)

    def __str__(self):
        return "\n".join(str(row) for row in self.data)

r, c = map(int, input("Enter rows and columns: ").split())

print("Enter Matrix A")
a = [list(map(int, input().split())) for _ in range(r)]

print("Enter Matrix B")
b = [list(map(int, input().split())) for _ in range(r)]

m1 = Matrix(a)
m2 = Matrix(b)

print("Addition")
print(m1 + m2)

print("Subtraction")
print(m1 - m2)

print("Multiplication")
print(m1 * m2)
