"""Последовательность треугольных чисел образуется путем сложения натуральных чисел.
К примеру, 7-ое треугольное число равно 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. Первые десять треугольных чисел:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
Перечислим делители первых семи треугольных чисел:
 1: 1
 3: 1, 3
 6: 1, 2, 3, 6
10: 1, 2, 5, 10
15: 1, 3, 5, 15
21: 1, 3, 7, 21
28: 1, 2, 4, 7, 14, 28
Как мы видим, 28 - первое треугольное число, у которого более пяти делителей.
Каково первое треугольное число, у которого более пятисот делителей?"""

number = 1
triangular_number = 0
divider_list = []

# while True:
#     triangular_number = int((number * (number + 1)) / 2)
#     for i in range(1, triangular_number + 1):
#         if triangular_number % i == 0:
#             divider_list.append(i)
#     print(number, triangular_number, len(divider_list), divider_list)
#     if len(divider_list) > 500:
#         break
#     number += 1
#     triangular_number = 0
#     divider_list = []
# print(number, triangular_number, len(divider_list), divider_list)
# print(number)
# print(triangular_number)
# print(len(divider_list), divider_list)
