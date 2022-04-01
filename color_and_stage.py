
stage = {
    'japan': {'red', 'white'},
    'kg': {'red', 'yellow'},
    'ru': {'red', "white", "blue"},
    'usa': {'white', 'blue', 'red'},
    'kz': {"blue", 'yellow'}
}
while True:
    p = input("Enter the color(‘q’ to exit: ").lower()
    if p == 'q':
        print('program stopped')
        break
    for key, value in stage.items():
        if set(p.split()).issubset(value):
            print(key)
