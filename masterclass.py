import random

list = ["камень", "ножницы", "бумага"]

while True:
    player = input("Выбери: камень, ножницы, бумага")
    bot = random.choice(list)

    if player.lower() =='выход':
        print('Игра завершена!')
        break

    if player == bot:
        print(f'Бот выбрал {bot}\n Вы выбрали {player}\n Ничья!')

    elif (bot == 'камень' and player == 'ножницы') or (bot == 'ножницы' and player == 'бумагу') or (bot == "бумага" and player == 'камень'):
        print(f'Бот выбрал {bot}\n Вы выбрали {player}\n Бот выиграл!')

    elif (player == 'камень' and bot == 'ножницы') or (player == 'ножницы' and bot == 'бумага') or (player == 'бумага' and bot == 'камень'):
        print()
        




