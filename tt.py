import random

count = 0

tries = int(input('Ведите количество попыток '))

while count != tries:
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    product = a * b
    try:
        answer = int(input(f'{a} * {b} = '))
        count += 1

        if answer != product:
            print(f'false! Ответ -{product}')
        else:
            print(f'true! Ответ - {product}')

        if tries != count:
            print(f'Количество оставшихся попыток - {tries - count}')

    except ValueError:
        print('Вводите только числа!!')

print("Игра окончена! Спасибо за игру <3")
