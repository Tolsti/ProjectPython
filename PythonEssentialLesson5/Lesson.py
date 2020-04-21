# values = [5, 8, 2, 1, 9, 2]
# print(values[1])
# print(values.__getitem__(1))
#
# print(values[2:5])
# print(values[slice(2, 5)])
# print(values.__getitem__(slice(2, 5)))


# import collections.abc
#
# print(dir(collections.abc.Sequence))


# def print_matrix(matrix):
#     for row in matrix:
#         print('  '.join(str(x) for x in row))
#
#
# # print_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#
# matrix = [[0] * 5 for _ in range(5)]
# print_matrix(matrix)
#
# print()
#
# matrix[1][3] = 1
# print_matrix(matrix)


# cities = ['Pytjnville', 'Darkmouth', 'Innport']
# print(cities)
# populations = [30000, 12400, 12300]
# print(populations)
#
# print(list(zip(cities, populations)))
# print(list(enumerate(cities)))
#
# a, b, c = 1, 2, 3
# print(a, b, c)
#
# a, b, c = range(3)
# print(a, b, c)
#
# a, b, c = 'qwe'
# print(a, b, c)
#
# x = 2
# y = 5
# print('x =', x, 'y =', y)
# x, y = y, x
# print('x =', x, 'y =', y)
#
# values = [5, 2, 1, 8, 3]
# for index, value in enumerate(values):
#     print('values[{}] = {}'.format(index, value))
#
# for city_number, city in enumerate(cities, 1):
#     print('City', city_number, 'is', city)


# def function(*args):
#     print(type(args))
#     print(args)
#
#
# function(1, 3, 5)
#
#
# def mean(first, *numbers):
#     sum_ = first + sum(numbers)
#     return sum_ / (len(numbers) + 1)
#
#
# print(mean(2, 3, 4))
# print(mean(2, 3, 4, 4, 15))
#
# values = [5, 2, 1, 8, 3]
# print(values)
# print(*values)


# print(range(10))
# print(range(2, 10))
# print(range(2, 10, 3))
# print(len(range(2, 10, 3)))
# print(len(range(20, 2, -3)))
# print(range(20, 2, -3)[1:5])


