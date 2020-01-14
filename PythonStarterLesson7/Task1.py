"""Создайте список и введите его значения. Найдите наибольший и наименьший элемент списка,
а также сумму и среднее арифметическое его значений."""

import random

lst = [random.randint(0, 100) for i in range(int(input('Количество элементов списка: ')))]
lst_min = 1000
lst_max = 0
lst_sum = 0
lst_arithmetic_mean = 0

for i in range(len(lst)):
    if lst[i] < lst_min:
        lst_min = lst[i]
    if lst[i] > lst_max:
        lst_max = lst[i]
    lst_sum += lst[i]
lst_arithmetic_mean = lst_sum / len(lst)

print('Полученный список:', lst)
print('Наименьший элемент:', lst_min)
print('Наибольший элемент:', lst_max)
print('Сумма элементов:', lst_sum)
print('Среднее арифметическое:', lst_arithmetic_mean)
