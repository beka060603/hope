def first_world(world='hello_world'):
    if type(world) == str:
        one_w = world.split()
        print(one_w[0])
    else:
        print(False,type(world))




sentence = str(input('введи предложение:'))
first_world(sentence)

def midle(*h):
    print(int(sum(h)/len(h)))

midle(1,5,8,8,8,88,9,0,00,0,0,0,0,9)

def passw(password):
    if len(password) > 6:
        if password.isdigit():
            print(False,1)
        elif password.isalpha():
            print(False,2)
        else:
            print(password)
    else:
        print(False,False)

passw('0000000000lkjhgh0')
