class Polynomial:
    def __init__(self, coeffs):
        self.coeffs = coeffs

    def __mul__(self, other):
        result = [0] * (len(self.coeffs) + len(other.coeffs) - 1)
        for i in range(len(self.coeffs)):
            for j in range(len(other.coeffs)):
                result[i + j] += self.coeffs[i] * other.coeffs[j]
        return Polynomial(result)

    def __str__(self):
        return str(self.coeffs)

p1 = Polynomial(list(map(int, input("Enter coefficients of first polynomial: ").split())))
p2 = Polynomial(list(map(int, input("Enter coefficients of second polynomial: ").split())))

print("Result:", p1 * p2)
