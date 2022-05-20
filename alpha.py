# 7.2 (7)
mony_course = float(input('Курс валюты к одному сому: '))
s = float(input('Количество'
                ' твоей валюты: '))
print(s * mony_course)

# 6.3(7)

k = list(range(-20, 31))
print('сумма:', sum(k), ', арифметическое:', len(k) // 2)
# 10 (7)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = int(input('число: '))
m = []
b = []

for i in arr:
    if num > i:
        m.append(i)
    elif num < i:
        b.append(i)
print((m), len(b))

# 6.3 (7)
dict_1, dict_2 = {'a': 100, 'b': 200}, {'c': 300, 'd': 400}
# print(dict_1 | dict_2)
#
# 5.2

s = input()
print(s.replace('o', '0')[::2])
# 5
m = 'мы обязательно научимся програмировать'
m2 = ' python'
m3 = m + m2
print(m[3], m[:5], m[::2], m[::3], m3, m[::-1], len(m))
#
#
# 5.3
l = list(range(0, 100)[::10])
g = list(range(0, 100)[::10])
l.pop(2)
g.pop(-1)
g.append(200)
h = l + g
new = h[7:16]
new.append(70)
new.append(80)
print(l)
print(g)
print(h)
print(new)
print(min(h), max(h))
# 6.1
a = tuple(range(1, 5)[::1])
b = ('dzumagulov', 'magarova', 'kaparov', 'm.baeva', 'kim')
print(b[4])
n = a + b
print(n)
new = n[2:6]
print(new)

# 6.2
school = {'1b': 22,
          '1u': 92,
          '1g': 2,
          '1h': 72,
          '1l': 19, }
print(school)

h = str(input('class: '))
for key, values in school.items():
    if set(h).issubset(key):
        print(values)
    else:
        print('такого нет')

school['1g'] = 19
school['1b'] = 10
school['1h'] = 19
school['3m'] = 7
school['0m'] = 70
school.pop('1u')
print(school)
