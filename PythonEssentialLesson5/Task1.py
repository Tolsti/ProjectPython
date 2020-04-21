"""Создайте функцию от произвольного количества аргументов, которая вычисляет среднее арифметическое данных чисел.
Вычислите при помощи неё среднее арифметическое двух заданных чисел и
среднее арифметическое чисел из заданного диапазона."""

numbers = list(range(10))
num1 = 2
num2 = 5


def function_arithmetic_mean(first, *number):
    sum_ = first + sum(number)
    return sum_ / (len(number) + 1)


print(function_arithmetic_mean(num1, num2))
print(function_arithmetic_mean(*range(2, 66)))
print(function_arithmetic_mean(*numbers))
