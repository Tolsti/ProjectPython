"""Напишите программу, которая вводит с клавиатуры текст и выводит отсортированные по алфавиту слова данного текста. """

my_string = 'At some point, you may need to break a large string down into smaller chunks, or strings. '\
            'This is the opposite of concatenation which merges or combines strings into one. To do this, '\
            'you use the split function. What it does is split or breakup a string and add the data to a string array '\
            'using a defined separator. If no separator is defined when you call upon the function, '\
            'whitespace will be used by default. In simpler terms, the separator is a defined character '\
            'that will be placed between each variable.'
print(my_string)

my_string = my_string.split(' ')
my_string.sort()
print(*my_string)

my_string = input('Input text:')
print('Input text:', my_string)

my_string = my_string.split(' ')
my_string.sort()
print('Sorted text:', *my_string)
