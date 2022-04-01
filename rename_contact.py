def create(name, phone):
    contains = False
    for i in contacts:
        if (i['name'] == name or i['phone'] == phone):
            contains = True
            break
    if (contains):

        print("Такой контакт уже есть")
    else:
        contacts.append({"name": name, 'phone': phone})


def edit(name, phone):
    inContact = False
    for i in contacts:
        if (i['name'] == name):
            inContact = True

            i['phone'] = phone
            break
    if (not inContact):
        print("такого имени в контакте нет")

def delete(name):
    inContact = False
    for i in contacts:
        if(i['name']==name):
            inContact = True
            contacts.remove(i)
    if(not inContact):
        print("Нельзя удалить то чего нет")

def showContacts():
    print()
    print("Список контактов")
    print()
    for i in contacts:
        print(*i.values())

contacts = [
    {'name': 'Geektech', 'phone': '0507052018'},
    {'name': 'Служба спасения', 'phone': '911'},
    {'name': 'Пожарная служба', 'phone': '101'},
]

create("Maktym", "0888234234")
create("Maktym", "0888234234")
create("Maktym", "088823423")
delete("Айдана")
delete("Maktym")
create("Айдана", "29428349924")
edit("Айданфвыа", "ыфвжалофыва")

create('dgvcj','6754678')
showContacts()