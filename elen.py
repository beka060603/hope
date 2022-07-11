import random
n = int(input('Введите n: '))
a = [[random.randint(-99, 99) for _ in range(n)] for __ in range(n)]
print(*a, sep='\n')
