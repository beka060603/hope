
class Fraction:

    def __init__(self, numerator, denumerator):
        self.num = numerator
        self.den = denumerator


    def __str__(self):
        return str(self.num) + '/' + str(self.den)

    def __add__(self, other):
        newNum = self.num * other.den + other.num * self.den
        newDenum = self.den * other.den
        newcom = Fraction(newNum,newDenum)
        return newcom

    def __sub__(self, other):
        newNum = self.num * other.den - other.num * self.den
        newDenum = self.den * other.den
        return Fraction(newNum, newDenum)

    def __mul__(self, other):
        newNum = self.num * other.num
        newDenum = self.den * other.den
        return Fraction(newNum, newDenum)

    def __floordiv__(self, other):
        newNum = self.num // other.num
        newDenum = self.den // other.den
        return Fraction(newNum, newDenum)

a = Fraction(3,9)
s= Fraction(2,6)
x= a+s
print(x.num)
print('--')
print(x.den)