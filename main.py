def pasw(password):
    if len(password)>6:
        if password.isdigit():
            print('пароль слишком легкий')
        elif password.isalpha():
            print('еще раз')
        else:
            print('пароль создан')
    else:
        print('вы должны ввести больше 6 символов')
a = input('введи пароль: ')
pasw(a)