# -*- coding: utf8 -*-
"""Создайте функцию-генератор чисел Фибоначчи.
Примените к ней декоратор, который будет оставлять в последовательности только чётные числа."""


def decorator_even(function):
    def decorator(num):
        return list(filter(lambda x: x % 2 == 0, function(num)))

    return decorator

# @decorator_even
def fibonacci(num):
    generator_fibonacci = []
    fib1, fib2 = 1, 1

    for _ in range(num):
        generator_fibonacci.append(fib1)
        fib1, fib2 = fib2, fib1 + fib2

    return generator_fibonacci


fib_100 = fibonacci(100)
print(fib_100)

fib_decor_100 = decorator_even(fibonacci)
print(fib_decor_100(100))
