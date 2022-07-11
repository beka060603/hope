guess = int(input("загадайте число от 0 до 100, программа попытается его отгадать!: "))
left = 1
right = 100
pop_it = 0

while True:
    current = (left + right) // 2
    is_right = input(f'Ваше число:{current}?(да, больше, меньше)')
    pop_it += 1
    if is_right == 'да':
        print('Я его угадал!', 'количество попыток:', pop_it)
        break
    elif is_right == 'больше':
        left = current
    else:
        right = current

