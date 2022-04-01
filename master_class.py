name = "Beka"

while True:
    a = float(input("Введите первое число:"))
    b = input("Введите операцию(+,-,*,/):")
    c = float(input("Введите второе число:"))

    if b == "+":
        answer = a+c

    elif b == "-":
        answer = a-c

    elif b == "*":
        answer = a*c

    elif b == "/" and c ==0:

        print("нельзя делить на 0")

    elif b == "/":
        answer = a/c

    else:
        print("не опознанная операция")

    print(f"вывод:{answer}")


