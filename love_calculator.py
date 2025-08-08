def calculate_love_score(name1, name2):
    x = 0
    y = 0
    a = 0
    b = 0

    for letter in name1.lower():
        if letter in 'true':
            x += 1
        if letter in 'love':
            a += 1
    for letter in name2.lower():
        if letter in 'true':
            y += 1
        if letter in 'love':
            b += 1


    print(f'{x + y}{a + b}')


name1 = input('enter first name: ')
name2 = input('enter second name: ')

calculate_love_score(name1,name2)
