
while True: 
    x, y = input('dale: ').split()
    x = int(x)
    y = int(y)
    if x == 0 or y == 0:
        break
    elif x > 0 and y > 0:
        print('primeiro')

    elif x < 0 and y > 0:
        print('segundo')

    elif x < 0 and y < 0:
        print('terceiro')

    elif x > 0 and y < 0:
        print('quarto')
    


