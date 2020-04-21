"""Напишите программу, которая вводит с клавиатуры последовательность чисел и
выводит её отсортированной в порядке возрастания."""

numbers = []

print('Enter a sequence of numbers if you want to finish writing:', *['exit', 'stop', 'quit'])

while True:
    try:
        number = input('Enter a number: ')
        if number in ['exit', 'stop', 'quit']:
            print('The resulting sequence:', numbers)
            numbers.sort()
            print('The sorted sequence:', numbers)
            break
        numbers.append(int(number))
    except ValueError:
        print('\"{}\" you entered is not a number!!!'.format(number))
