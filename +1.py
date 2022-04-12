while True:
    n1 = int(input('введите 1 число:'))
    n2 = int(input('введите 2 число:'))
    nn1 = n1 + n2
    if n1 > n2:
        g = n1 - n2
        print('разница между ними:', g)
    elif n1 == n2:
        print('оба числа равны:', n1)
    else:
        print('сумма чисел равнается:', n1)





a = int(input('введи а'))
b = int(input('введи а'))
c = int(input('введи а'))
x = int(input('введи а'))
if c < 0 or x != 0:
    print(a * x - c)
elif c > 0 or x == 0:
    print(x - a / -c)
else:
    print(b * x / c - a)



x = int(input("Длина стороны квадрата : "))
s = input("Символ : ")
for i in range(x):
    tmp = [s if i == j or x - i - 1 == j else ' ' for j in range(x)]
    print(''.join(tmp))




N = int(input())
s = [int(input()) for i in range(N)]
print(min(s))


def sum_gp(a, q, n):
    if n == 0:
        return 0
    else:
        return a + sum_gp(a * q, q, n - 1)


print(sum_gp(1, 2, 5))
