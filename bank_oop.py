class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Jack(Person):

    def __init__(self, phone_number, first_name, last_name, balance):
        super().__init__(first_name, last_name)
        self.phone_number = phone_number
        self.balance = balance


h = Jack('jack', 'd', 'd', 1000)


class Vito(Jack):
    __balance = 100

    def __init__(self, phone_number, first_name, last_name, balance):
        super().__init__(phone_number, first_name, last_name, balance)

    def minus(self):
        o = h.balance - self.__balance
        var = self.balance + o
        print(var)


g = Vito('vito', 'd', 'd', 10)

Vito.minus(g)

