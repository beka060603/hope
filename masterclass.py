import random

lst = ['камень', 'ножницы', 'бумага']
while True:
    play = input('Введите (камень, ножницы, бумага):').lower()
    bot = random.choice(lst)
    if play == 'выход':
        print('Пргогрмма завершена')
        break
    if play == bot:
        print(f'bot choosed - {bot}\n You winned-{play}\n ничья')

    elif (bot == 'камень' and play == 'ножницы') or (bot == 'ножницы' and play == 'бумага') or (
            bot == 'бумага' and play == 'камень'):
        print(f'bot choosed - {bot}\n You выбрали-{play}\n Бот выиграл')

    elif (bot == 'бумага' and play == 'ножницы') or (bot == 'камень' and play == 'бумага') or (
            bot == 'ножницы' and play == 'камень'):
        print(f'bot choosed - {bot}\n You выбрали-{play}\n Вы выиграл')

    else:
        print("Неправильная команда")
