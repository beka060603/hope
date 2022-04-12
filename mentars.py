# mentor = ['Эсенбек', 'Мирхад', 'Беки']
# while True:
#     if len(mentor) <= 5:
#         command = input(
#             f'{mentor}\n'
#             f'Выберите команду: \n '
#             f'1 - добавление \n '
#             f'2 - изменение \n '
#             f'3 - удаление \n '
#             f'4 - выход \n:')
#         if command == '4':
#             print(tuple(mentor))
#             break
#
#         elif command == '1':
#             new_mentor = input('\nВведи имя ментора, которого вы хотите добавить: ').capitalize()
#             if new_mentor in mentor:
#                 print("этот ментор уже есть в списке")
#             elif len(new_mentor) <= 15:
#                 mentor.append(new_mentor)
#                 print(mentor)
#             else:
#                 print('\n Имя должно содержать не более 15 букв')
#                 continue
#
#         elif command == '2':
#             changed_mentor = input('\n Введи имя ментора, ты хочешь заменить: ').capitalize()
#             added_mentor = input('\n Введи имя нового ментора:').capitalize()
#             if changed_mentor in mentor and len(added_mentor) <= 15:
#                 mentor.remove(changed_mentor)
#                 mentor.append(added_mentor)
#             elif changed_mentor in mentor and len(added_mentor) != 15:
#                 print('\n Имя должно содержать не более 15 букв')
#                 continue
#             else:
#                 print('\n Ментора, которого вы хотите изменить, нет в списке')
#                 continue
#
#         elif command == '3':
#             remove_mentors = input(
#                 '\n Введите имя ментора или индекс, которого вы хотите удалить из списка: ').capitalize()
#             if remove_mentors in mentor:
#                 mentor.remove(remove_mentors)
#                 mentor.pop(remove_mentors in mentor)
#             else:
#                 print('\n Ментора, которого вы хотите удалить, нет в списке')
#                 continue
#     else:
#         print(' \n список не имеет быть больше 5 менторов \n')
#         break
#
#


mentors = ['Эсенбек', 'Мирхад', 'Беки']
while True:
    menu = input(' \n 1-Добавление : \n 2-Изменение : \n 3-Удаление : \n 0-Выход : \n')
    if menu == '1':
        print('Добавление:')
        name = input('name').capitalize()
        if len(mentors) <= 4:
            if len(name) >= 15:
                print('Слишком много букв!')
            else:
                mentors.append(name)
                print(mentors)
        else:
            print('Слишком много ментаров!')
    elif menu == '2':
        print('Изменение:')
        if menu == '2':
            zamena = input('Введите имя, которую хотите заменить:').capitalize()
            new = input('Новое имя:').capitalize()
            print(mentors)
            if zamena in mentors and len(new) <= 15:
                mentors.remove(zamena)
                mentors.append(new)
            elif zamena in mentors and len(new) != 15:
                print('Имя больше 15 букв!')
            else:
                print('Такого ментора нет!')
    elif menu == '3':
        print('Удаление:')
        if menu == '3':
            delete = input('Введите имя или индекс')
            if delete == 'индекс':
                delete = int(input('индекс'))
                if delete > len(mentors) - 1:
                    print('Такого индекса нет!')
                    continue
                else:
                    del mentors[delete]
            elif delete == 'name':
                name1 = input('name:')
                if name1 in mentors:
                    mentors.remove(name1)
                    print(mentors)
                else:
                    print('Такого ментора нет!')
            else:
                print('Такой команды нет!')
                continue
    elif menu == '0':
        list = tuple(mentors)
        print(list)
        break
    else:
        print('Есть команды: 1, 2, 3, 0!')