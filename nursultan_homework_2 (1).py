min = 0
max = 100
attempts = 0
while True:
    n = (min+max)//2
    answer = input(f"это ваше число?(больше/меньше/да): {n}")
    if answer == "больше":
        min = n
        attempts += 1
    elif answer == "меньше":
        max = n
        attempts += 1
    elif not answer == ("больше","меньше","да"):
        print("вводите только больше/меньше/да!")
    elif answer in "да":
        attempts += 1
        print(f"ваше число {n}, попыток: {attempts}!")
        break