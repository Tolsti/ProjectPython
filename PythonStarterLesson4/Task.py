"""Создайте программу, которая рисует на экране прямоугольник из звёздочек
заданной пользователем ширины и высоты."""
tmp_a = int(input('Введите ширину: '))
tmp_b = int(input('Введите длину: '))
while tmp_a > 0:
    b = tmp_b
    while b > 0:
        print('*', end = ' ')
        b -= 1
    print()
    tmp_a -= 1
