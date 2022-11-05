x = float(input('Введите число для x: '))
y = float(input('Введите число для y: '))

if x == y:
    print('x и y равны')
    if y != 0:
        print(f'Следовательно, x/y равно {x/y}')
    elif x > y:
        print('x больше y')
    else:
        print('y больше x')
    print("Спасибо!")