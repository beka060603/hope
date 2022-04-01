class Fraction:

    def __init__(self, numertor, denumerator):
        self.num = numertor
        self.den = denumerator

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, other):
        newnum = self.num * other.den + \
                 self.den * other.num
        newden = self.den * other.den
        common = (newnum, newden)
        return Fraction(newnum // common,
                        newden // common)

    def __sub__(self, other):
        newnum = self.num * other.den - \
                 self.den * other.num
        newden = self.den * other.num
        common = (newnum, newden)
        return Fraction(newnum // common,
                        newden // common)

    def __mul__(self, other):
        newnum = self.num * other.den * \
                 self.den * other.num
        newden = self.den * other.num
        common = (newnum, newden)
        return Fraction(newnum // common,
                        newden // common)

    def __floordiv__(self, other):
        newnum = self.num * other.den // \
                 self.den * other.num
        newden = self.den * other.num
        common = (newnum, newden)
        return Fraction(newnum // common,
                        newden // common)


d = Fraction(1, 8)
f = Fraction(1, 7)
dh=d+f
print(dh.num)
print(dh.den)

