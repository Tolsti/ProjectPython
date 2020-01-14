"""Простым называется число, которое делится нацело только на единицу и само себя.
Число 1 не считается простым. Напишите программу, которая находит все простые числа в заданном промежутке,
выводит их на экран, а затем по требованию пользователя выводит их сумму либо произведение."""

import numpy

number = int(input("Введите число: "))
lst_prime_number = [i for i in range(number)]

for i in lst_prime_number[2:]:
    for j in range(i + i, len(lst_prime_number), i):
        lst_prime_number[j] = 0
lst_prime_number = [i for i in lst_prime_number[2:] if i != 0]
print(lst_prime_number,
      '\nВывести сумму простых чисел: +',
      '\nВывести произведение простых чисел: *')
operation = input('Ввведите оперцию: ')

if operation == '+':
    print('Сумма простых чисел:', sum(lst_prime_number))
elif operation == '*':
    print('Произведение простых чисел:', numpy.prod(lst_prime_number))
else:
    print('Нет такой операции')
