# # def add(x, y):
# #     return x + y
# #
# #
# # def sub(x, y):
# #     return x - y
# #
# #
# # def mul(x, y):
# #     return x * y
# #
# #
# # def div(x, y):
# #     return x / y
# #
# #
# # operations = {
# #     '+': add,
# #     '-': sub,
# #     '*': mul,
# #     '/': div,
# #     '^': pow
# #     }
#
# operations = {
#     '+': lambda x, y: x + y,
#     '-': lambda x, y: x - y ,
#     '*': lambda x, y: x * y,
#     '/': lambda x, y: x / y,
#     '^': pow
#     }
#
# try:
#     first = float(input('First number: '))
#     operation = input('Operation: ')
#     second = float(input('Second number: '))
#     result = operations[operation](first, second)
# except ValueError:
#     print('Incorrect input')
# except KeyError:
#     print('Unsupported operation')
# except ZeroDivisionError:
#     print('Division by zero')
# else:
#     print('Result', result)


# * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * #


# def add(x):
#     def do_add(y):
#         return x + y
#
#     return do_add
#
#
# print(add(5)(3))
#
# add_to_five = add(5)
# print(add_to_five(3))
# print(add_to_five(10))


# * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * #


# def Person(name, age):
#     def print_hello():
#         print('Hello! My name is {}'.format(name))
#
#     def get_age():
#         return age
#
#     return {'print_hello': print_hello, 'get_age': get_age}
#
#
# john = Person('John', 28)
# john['print_hello']()
# print(john['get_age']())


# * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * #


# elem = lambda value, next: {'value': value, 'next': next}
# to_string = lambda head: '' if head is None \
#                             else str(head['value']) + ' ' + to_string(head['next'])
#
# values = elem(1, elem(2, elem(3, None)))
# print(to_string(values))


# * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * #


# def make_powers(count):
#     powers = []
#     for i in range(count):
#         powers.append(lambda x: x ** i)
#     return powers
#
#
# powers = make_powers(5)
# for power in powers:
#     print(power(2), end=' ')
# print()
#
#
# def make_powers1(count):
#     powers = []
#     for i in range(count):
#         powers.append((lambda p: lambda x: x ** p)(i))
#     return powers
#
#
# powers = make_powers1(5)
# for power in powers:
#     print(power(2), end=' ')
# print()
#
#
# def make_powers2(count):
#     powers = []
#     for i in range(count):
#         powers.append(lambda x, p=i: x ** p)
#     return powers
#
#
# powers = make_powers2(5)
# for power in powers:
#     print(power(2), end=' ')
# print()
#
#
# def make_powers3(count):
#     powers = []
#     for i in range(count):
#         powers.append(lambda x, i=i: x ** i)
#     return powers
#
#
# powers = make_powers3(5)
# for power in powers:
#     print(power(2), end=' ')
# print()


# * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * #


# # in applied code:
# handlers = []
# for i in range(1, 4):
#     def on_click(i=i):
#         print('Button {} clicked'.format(i))
#
#
#     handlers.append(on_click)
#
# # in event loop
# for handler in handlers:
#     handler()


# * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * #


# # def decorator(fn):
# #     def decorated_fn(*args, **kwargs):
# #         print('Starting decorated function')
# #         fn(*args, **kwargs)
# #         print('End of decorated function')
# #
# #     return decorated_fn
#
# def make_decorator(string):
#     def decorator(fn):
#         def decorated_fn(*args, **kwargs):
#             print(string)
#             fn(*args, **kwargs)
#
#         return decorated_fn
#
#     return decorator
#
#
# @make_decorator('Before invocation')
# @make_decorator('Another decorator')
# def print_hello():
#     print('Hello!!!')
#
#
# print_hello()


# * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * #


# from functools import reduce
#
# values = [2, 1, 5, 8, 3, 2]
# print(*[i ** 2 for i in values])
# print(*list(map(lambda x: x ** 2, values)))
# for square in map(lambda x: x ** 2, values):
#     print(square, end=' ')
# print()
#
# values = [4, -1, 2, 0, 5, 3, -3]
# positive = list(filter(lambda x: x > 0, values))
# print(*positive)
#
# values = [4, -1, 2, 5, 3, -3]
# product = reduce(lambda x, y: x * y, values)
# print(product)


# * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * #


# from functools import lru_cache
#
#
# @lru_cache(maxsize=None)
# def fibonacci(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# for i in range(1, 100):
#     print(i, fibonacci(i))


# * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * #


# from functools import partial
#
#
# def add(x, y):
#     return x + y
#
#
# add_to_five = partial(add, 5)
# print(add_to_five(3))
# print(add_to_five(5))
#
# print_with_comma = partial(print, sep=', ')
# print_with_comma(1, 2, 3)


# * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * #


# from itertools import chain
# from itertools import product
#
# for i in range(1, 5):
#     for j in range(1, 5):
#         print('{} x {} = {}'.format(i, j, i * j), end=' ')
# print()
#
# for i, j in product(range(1, 5), range(1, 5)):
#     print('{} x {} = {}'.format(i, j, i * j), end=' ')
# print()
#
# for i in chain(range(1, 5), range(1, 5)):
#     print(i, end=' ')


# * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * #


# from itertools import combinations
# from itertools import combinations_with_replacement
# from itertools import permutations
#
# string = 'ABC'
# elements = 2
#
# print(list(permutations(string, elements)))
# print(list(combinations(string, elements)))
# print(list(combinations_with_replacement(string, elements)))


# * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * #


# from itertools import dropwhile
# from itertools import takewhile
#
# values = [1, 4, 3, 5, 3, 2, 8]
# predicate = lambda x: x < 5
#
# for elem in takewhile(predicate, values):
#     print(elem, end=' ')
# print()
#
# for elem in dropwhile(predicate, values):
#     print(elem, end=' ')


# * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * #


# from operator import neg
#
# values = [5, 2, 1, 3, 8, -3]
# print(*list(map(neg, values)))
# print(*list(map(lambda x: -x, values)))
# for i in values:
#     print(neg(i), end=' ')
