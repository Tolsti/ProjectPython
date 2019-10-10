"""Напишите программу-калькулятор, в которой пользователь сможет ввести выбрать операцию,
ввести необходимые числа и получить результат. Операции,
которые необходимо реализовать: сложение, вычитание, умножение, деление,
возведение в степень, синус, косинус и тангенс числа."""
import math

while True:
    result = None
    print('-------------------------------------------------------------------------')
    tmp_operation = str(input('+ сложение, - вычитание, * умножение, / деление, ** возведение в степень, '
                              '\nsin синус, cos косинус, tan тангенс, e выход из программы'
                              '\nВведите операцию: '))
    if tmp_operation == 'e':
        print('Программа закрыта.')
        break
    elif tmp_operation == '+' or tmp_operation == '-' or tmp_operation == '*' or tmp_operation == '/' or tmp_operation == '**':
        print('Введите два числа для операции.')
        tmp_a = int(input('Введите первое число: '))
        tmp_b = int(input('Введите второе число: '))
        if tmp_operation == '+':
            result = tmp_a + tmp_b
        if tmp_operation == '-':
            result = tmp_a - tmp_b
        if tmp_operation == '*':
            result = tmp_a * tmp_b
        if tmp_operation == '/':
            result = tmp_a / tmp_b
        if tmp_operation == '**':
            result = tmp_a ** tmp_b
    elif tmp_operation == 'sin' or tmp_operation == 'cos' or tmp_operation == 'tan':
        tmp_a = int(input('Введите число: '))
        if tmp_operation == 'sin':
            result = math.sin(tmp_a)
        if tmp_operation == 'cos':
            result = math.cos(tmp_a)
        if tmp_operation == 'tan':
            result = math.tan(tmp_a)
    else:
        print('Такой операции нет.')
    print('Результат действия: ' + str(result))
