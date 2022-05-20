

username = input("Введите свое никнейм: ")

name = input("Введите свое имя: ")

surname = input("Введите свою фамилию: ")


'esenbekm03@gmail.com'

while True:
    gmail = input("Введите свой gmail: ")

    if gmail[-10:] != "@gmail.com":
        print("Почта должна содержать @gmail.com!")
    else:
        break


"+996555333222"

while True:
    phone = input("Введите номер телефона: ")

    if phone[:4] != '+996':
        phone = '+996' + phone
        break
    else:
        break

while True:
    password1 = input("Введите пароль: ")
    password2 = input("Повторите пароль: ")

    if password1 != password2:
        print("Пароли не совподают!")
    else:
        break


user = dict(
    username=username,
    name=name,
    surname=surname,
    gmail=gmail,
    phone=phone,
    password=password2
)

print(user)
