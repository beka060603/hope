import random
a= random.randint(1,10)
pop=3
print(a)
while 1:
    if pop >0:
        pop-=1
        f=int(input('я загадал число,угадай за 3 попытки:'))
        print(f'у тебя {pop} попыток')
        if f ==a:
            print('ты угодал')
            break
    else:
        print('попытки кончились')
        break
# 1 задание
while 1:
    s=input('должность:')
    л=input('компания:')
    в=input('фио:')
    print('*********')
    print("*",s,"*")
    print("*",л,"*")
    print("*",в,"*")
    print('*********')
    break

# таблица умножения
cum=int(input('введи число'))
for i in range(1,11):
    h=cum*i
    print(h)