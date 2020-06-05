"""Модифицируйте решение предыдущего задания так, чтобы оно работало не с текстовыми, а бинарными файлами."""

import random

with open('data/numbers.bin', 'wb') as data:
    data.write('\n'.join(str(random.uniform(0, 100)) for _ in range(10000)).encode())

with open('data/numbers.bin', 'rb') as data:
    num = []
    for number in data:
        print(float(number))
        num.append(float(number))
    print('Sum:', sum(num))
