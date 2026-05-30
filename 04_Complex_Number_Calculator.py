class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __str__(self):
        return f"{self.real}+{self.imag}i"

r1, i1 = map(int, input("Enter first complex number: ").split())
r2, i2 = map(int, input("Enter second complex number: ").split())

c1 = Complex(r1, i1)
c2 = Complex(r2, i2)

print("Addition:", c1 + c2)
print("Subtraction:", c1 - c2)
