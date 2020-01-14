"""Используя вложенные циклы и функции print(‘*’, end=’’), print(‘ ‘, end=’’) и print()
выведите на экран прямоугольный треугольник."""
tmp_size = int(input())

for i in range(0, tmp_size):
    for j in range(0, i):
        print('*', end=' ')
    print('*')
