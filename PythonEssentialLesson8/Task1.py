"""Напишите скрипт, который создаёт текстовый файл и записывает в него 10000 случайных действительных чисел.
Создайте ещё один скрипт, который читает числа из файла и выводит на экран их сумму. """

import random

with open('data/numbers.txt', 'w') as data:
    data.write('\n'.join([str(random.uniform(0, 100)) for number in range(10000)]))

with open('data/numbers.txt') as data:
    for i in data.readlines():
        print(float(i))
    data.seek(0)
    print(sum([float(i) for i in data]))
