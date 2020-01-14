"""Напишите рекурсивную функцию, которая вычисляет сумму натуральных чисел,
которые входят в заданный промежуток."""


def fun_recurs(a):
    if a <= 0:
        print('\nСумма последовательности: ', end='')
        return 0
    print(a, end=" ")
    return fun_recurs(a - 1) + a


tmp_num = int(input('Введите число: '))
print(fun_recurs(tmp_num))
