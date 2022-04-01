us = ' `qwertyuiop[]asdfghjkl;"zxcvbnm,.'
ru = ' ёйцукенгшщзхъфывапролджэячсмитьбю'
while True:
    n = input('\nведи букву, для выхода намжми 1\n')
    if n =='1':
        print('программа завершина')
        break
    for i in n:
        if i in us:
            index1 = us.index(i)
            r = ru[index1]
            print(r,end='')
        else:
            index2 = ru.index(i)
            u = us[index2]
            print(u,end='')