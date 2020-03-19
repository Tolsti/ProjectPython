"""Напишите программу-калькулятор, которая поддерживает следующие операции: сложение, вычитание, умножение,
деление и возведение в степень. Программа должна выдавать сообщения об ошибке и
продолжать работу при вводе некорректных данных, делении на ноль и возведении нуля в отрицательную степень."""

print('Программа калькулятор:')
print('+ : сложение')
print('- : вычитание')
print('* : умножение')
print('/ : деление')
print('** : возведение в  степень')
print()

while True:
    a = None
    b = None
    operation = None
    result = None
    
    while True:
        try:
            a = int(input('Введите первое число: '))
            b = int(input('Введите второе число: '))
            break
        except ValueError:
            print()
            print('Введите цифры!!!')
            print()
    
    try:
        operation = input('Введите операцию: ')
        if operation == '+':
            result = a + b
        elif operation == '-':
            result = a - b
        elif operation == '*':
            result = a * b
        elif operation == '/':
            result = a / b
        elif operation == '**':
            result = a ** b
        else:
            raise SystemExit
        
        print()
        print('Результат вычисления:', result)
        
        break
    except ZeroDivisionError:
        print()
        print('НЕЛЬЗЯ!!!')
        print('Делить на ноль')
        print('Возводить ноль в отрицательеую степень')
        print()
    except SystemExit:
        print()
        print('Нет такой операции!!!')
        print()
