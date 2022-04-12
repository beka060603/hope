n = int(input('Задайте число для вычета/добавления от/к баланса/у: '))


class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Jack(Person):

    def __init__(self, first_name, last_name, phone_number, balance):
        super().__init__(first_name, last_name)
        self.phone_number = phone_number
        self.balance = balance

    def addition(self):
        self.balance += n
        print(f'Jack balance = {self.balance}')


class Vito(Jack):

    def __init__(self, first_name, last_name, phone_number, balance):
        super().__init__(first_name, last_name, phone_number, balance)

    def deduction(self):

        if self.balance >= n:
            self.balance -= n
            print(f'Vito balance = {self.balance}')
            # Как здесь из Jack balance вычесть ???

        else:
            print(f'Ваш баланс недостаточен для подключения услуги в {n} сом')


wer = Jack('Jack', 'Fergusson', '0553545454', 100)
der = Vito('Vito', 'Corleone', '0778252525', 50)

der.deduction()
wer.addition()
der.deduction()
wer.addition()
der.deduction()
wer.addition()