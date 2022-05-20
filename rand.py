from datetime import datetime as dt
start = dt.now()
end = dt.now()
print(start)
from random import randint as rd
attempts = 0
numb = ""
random = rd(1, 101)
while numb != random:
    try:
        attempts +=1
        numb = int(input('Введите число:'))
        print(random)
      
        if numb < random:
            print('Меньше чем {random}')
            continue
        elif numb > random:
            print('Больше чем {random}')
            continue
       
        else:
            print('Ты угадал число, которое я загадал')
            break
       
    except IndexError:
        print('Вводите только числа 0 до 100')
        attempts -=1
    except ValueError:
        print('Только цифры')
        attempts-=1
    except SyntaxError:
        attempts-=1
        print('hh')
result = (dt.now() - start)
print(f'Время игры: str(result)'.format())
print(f'Количество попыток: {attempts}')

