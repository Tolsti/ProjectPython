# import fibonacci
#
# print(fibonacci.__name__)
#
# index = int(input('Fibonacci number '))
# print(fibonacci.nth_fibonacci(index))


# * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * #


# from fibonacci import nth_fibonacci
#
# index = int(input('Fibonacci number '))
# print(nth_fibonacci(index))


# * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * #


# import fibonacci
#
# nth_fibonacci = fibonacci.nth_fibonacci
# del fibonacci
#
# index = int(input('Fibonacci number '))
# print(nth_fibonacci(index))


# * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * #


# from fibonacci import nth_fibonacci as fib
#
# index = int(input('Fibonacci number '))
# print(fib(index))


# * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * #


# from ProjectPython.PythonEssentialLesson7.fibonacci import *
#
# index = int(input('Fibonacci number '))
# print(nth_fibonacci(index))
#
# fibonacci_sequence()
# fibonacci(10)


# * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * #


# import copy
#
#
# class Container:
#     def __init__(self):
#         self.list = [1, 2, 3]
#         self.number = 8
#
#
# obj = Container()
# print(obj.list)
# print(obj.number)
#
# obj_copy = copy.copy(obj)
# obj_copy.list.append(4)
# print(obj_copy.list)
# print(obj.list)
#
# obj_deepcopy = copy.deepcopy(obj)
# obj_deepcopy.list.append(5)
# print(obj_deepcopy.list)
# print(obj.list)


# * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * #


# import random
#
# print(random.random())
# print(random.random())
# print(random.random())
#
# print(random.randint(1, 100))
# print(random.randint(1, 100))
# print(random.randint(1, 100))
#
# print(random.choice(['first', 'second', 'third']))
# print(random.choice(['first', 'second', 'third']))
# print(random.choice(['first', 'second', 'third']))
#
# print(random.sample(range(100), 10))
# print(random.sample(range(10), 5))
# print(random.sample(range(3), 3))


# * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * #


# from decimal import Decimal
# from fractions import Fraction
#
# print(0.1 + 0.2)
# print(Decimal('0.1') + Decimal('0.2'))
#
# print(2 ** 0.5)
# print(Decimal(2) ** Decimal(0.5))
#
# print(1.3465 * 5.18)
# print(Decimal('1.3465') * Decimal('5.18'))
#
# print(1 / 3)
# print(Decimal(1) / Decimal(3))
# print(Fraction(1, 3))
#
# print(Fraction(5, 8) * Fraction(1, 3) - Fraction(17, 28))
# print(Fraction(1, 2) + Fraction(1, 2))
# print(Fraction(2, 3) ** 3)
# print(Fraction(2, 3) ** Fraction(1, 2))


# * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * #


# import datetime
#
# now = datetime.datetime.now()
# print(now)
# # print(input())
# print(datetime.datetime.now() - now)
# print((datetime.datetime.now() - now) * 5)
#
# some_day = datetime.datetime(year=1986, month=2, day=2)
# print(some_day)
# print((datetime.datetime.now() - some_day))
#
# some_day = datetime.datetime(year=2015, month=5, day=18, hour=0, minute=23, second=18)
# print(some_day)
# some_day += datetime.timedelta(days=2, hours=3)
# print(some_day)
# some_day -= datetime.timedelta(hours=4)
# print(some_day)
# print(some_day.strftime('%A, %d.%m.%Y'))
