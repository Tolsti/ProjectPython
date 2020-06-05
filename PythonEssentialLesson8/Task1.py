"""Напишите скрипт, который создаёт текстовый файл и записывает в него 10000 случайных действительных чисел.
Создайте ещё один скрипт, который читает числа из файла и выводит на экран их сумму. """

import random

with open('data/numbers.txt', 'w') as data:
    data.write('\n'.join([str(random.uniform(0, 100)) for number in range(10000)]))

with open('data/numbers.txt') as data:
    num = []
    for i in data.readlines():
        num.append(float(i))
        print(float(i))
    print('Sum:', sum(num))
