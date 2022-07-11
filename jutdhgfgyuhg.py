import random

h = 'загадайте число'
print(h)
t = 100
g = 'ваше число 50?'
gh = 50
name = input('"<"">" or "да"')
i = 0
while i:
    i += 1
    if name == '>':
        gh_r = random.randint(gh, t)
        print(gh_r)
    elif name == "<":
        gh_r = random.randint(0, gh)
    elif name == "да":
        print(f'отгадали число это {gh}! количество попыток составило: ', i)
    with open('results.txt', 'a') as file:
        file.write(f"кол-во попыток: {i}\n"
                   f"попытки: {gh}\n"
                   f"загаданное число: {gh}")
        break
