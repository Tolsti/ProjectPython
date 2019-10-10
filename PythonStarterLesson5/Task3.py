import random

"""Создайте программу-калькулятор, которая поддерживает четыре операции:
сложение, вычитание, умножение, деление.
Все данные должны вводиться в цикле, пока пользователь не укажет,
что хочет завершить выполнение программы.
Каждая операция должна быть реализована в виде отдельной функции.
Функция деления должна проверять данные на корректность и выдавать
сообщение об ошибке в случае попытки деления на ноль."""


def function_addition(a, b):
    return a + b


def function_subtraction(a, b):
    return a - b


def function_multiplication(a, b):
    return a * b


def function_division(a, b):
    if b == 0:
        return print('Делить на ноль нельзя.')
    else:
        return a / b


while True:
    flag = None
    print('---------------------------------------------------------------------')
    operation_tmp = input('+ сложение, - вычитание, * умножение, / деление, e выйти из программы'
                          '\nВведите нужную операцию: ')
    if operation_tmp == 'e':
        break
    if operation_tmp == '+' or operation_tmp == '-' or operation_tmp == '*' or operation_tmp == '/':
        parameter_a = int(input('Введите первый параметр: '))
        parameter_b = int(input('Введите второй параметр: '))
        if operation_tmp == '+':
            flag = function_addition(parameter_a, parameter_b)
        elif operation_tmp == '-':
            flag = function_subtraction(parameter_a, parameter_b)
        elif operation_tmp == '*':
            flag = function_multiplication(parameter_a, parameter_b)
        elif operation_tmp == '/':
            flag = function_division(parameter_a, parameter_b)
    else:
        print('Нет такой операции')
    
    print('Полученный результат: ' + str(flag))
