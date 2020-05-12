"""Создайте словарь с ключами-строками и значениями-числами.
Создайте функцию, которая принимает произвольное количество именованных параметров.
Вызовите её с созданным словарём и явно указывая параметры."""

dictionary = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
              'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'zero': 0}


def my_function(*args):
    return args


for i in my_function('eight'):
    print(dictionary[i], end=' ')
print()

for i in my_function('one', 'two', 'five', 'nine'):
    print(dictionary[i], end=' ')
print()

# * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * #

def my_function_1(first, *args):
    if len(args) == 0:
        result = [first]
    else:
        result = list(args)
        result.insert(0, first)
    return tuple(result)


for i in my_function_1('eight'):
    print(dictionary[i], end=' ')
print()

for i in my_function_1('one', 'two', 'five', 'nine'):
    print(dictionary[i], end=' ')
print()
print(tuple('1'))
