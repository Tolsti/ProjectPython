x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))
operation = input('Введите оператор: ')
result = None

if operation == '+':
    result = x + y
elif operation == '-':
    result = x - y
elif operation == '*':
    result = x * y
elif operation == "/":
    result = x / y
else:
    print('Оператор не был введен!')

if result is not None:
    print('Оперция равна: ', result)
