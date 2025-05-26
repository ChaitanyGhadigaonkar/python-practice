class ComplexNumber:

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def conjugate(self):
        return ComplexNumber(self.real, -1 * self.imag)

    def __str__(self):  # dunder or magic methods
        if self.imag < 0:
            return f"({self.real}{self.imag}j)"
        else:
            return f"({self.real}+{self.imag}j)"

    def __add__(self, other):
        newReal = self.real + other.real
        newImag = self.imag + other.imag
        return ComplexNumber(newReal, newImag)

    def __sub__(self, other):
        newReal = self.real - other.real
        newImag = self.imag - other.imag
        return ComplexNumber(newReal, newImag)

    def __mul__(self, other):
        newReal = self.real * other.real - self.imag * other.imag
        newImag = self.real * other.imag + self.imag * other.real

        return ComplexNumber(newReal, newImag)

    def __truediv__(self, other):
        den = other.real ** 2 + other.imag ** 2
        return self * ComplexNumber(other.real / den, (-1 * other.imag)/den)

    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag


def main():
    c1 = ComplexNumber(1, 3)
    c2 = ComplexNumber(1, -3)
    a = 1
    b = 2 - 5j

    print(c1 + c2)
    print(c1 - c2)
    print(c1 * c2)
    print(c1 / c2)
    print(c1 == c2)


main()
