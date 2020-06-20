"""Создайте обычную функцию умножения двух чисел. Частично примените её к одному аргументу.
Создайте каррированную функцию умножения двух чисел. Частично примените её к одному аргументу."""

from functools import partial


def multiplication(x, y):
    return x * y


new_multiplication = partial(multiplication, 23)

print(multiplication(23, 81))
print(new_multiplication(81))


def curried_multiplication(x):
    def multi(y):
        return x * y

    return multi


new_curring_multiplication = partial(curried_multiplication(23))

print(curried_multiplication(23)(81))
print(new_curring_multiplication(81))
