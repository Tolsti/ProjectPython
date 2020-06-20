"""Создайте список целых чисел. Получите список квадратов нечётных чисел из этого списка."""

import random

list_of_integers = [random.randint(1, 100) for _ in range(100)]
print(*list_of_integers)


def list_of_odd_number_squares(lst):
    return [i ** 2 for i in lst if i % 2 != 0]


print(*list_of_odd_number_squares(list_of_integers))
