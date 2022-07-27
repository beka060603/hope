name=input('введи имя: ')
lasName=input('введи фамилию :')
password=input('введите пароль: ')
def test(password):
    if len(password) > 8:
        if password.isdigit():
            print('пароль должен быть с буквами и цифрами')
        elif password.isalpha():
            print('пароль должен состоять из цифр и букв')
        else:
            print(password)
    else:
        print('пароль должен быть больше 8 символов')


test(password)
print('ваше имя:',name)
print('ваша фамилия:', lasName)
print('ваш пароль:',password)
print('данные сохранены')