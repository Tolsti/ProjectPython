"""Ещё раз разберите все примеры к уроку, повторите теорию и ознакомьтесь с документацией по рассмотренным модулям."""

import functools
import itertools
import random

values = [random.randint(1, 10) for _ in range(10)]
print(values)

print(list(map(lambda x: x ** 2, values)))
print(list(filter(lambda x: x >= 5, values)))
print(functools.reduce(lambda x, y: x + y, values))

print(list(itertools.permutations('qwerty', 6)))
print(list(itertools.combinations('qwerty', 3)))
print(list(itertools.combinations_with_replacement('qwerty', 6)))


def decorator_neg(function):
    def decorator(num):
        if type(num) == int:
            return -function(num)
        elif type(num) in [list, tuple]:
            return list(map(lambda x: -x, function(num)))

    return decorator


@decorator_neg
def number(num):
    return num


number_decor = decorator_neg(number)

print(number(67))
print(number_decor((9, 32, -90)))
