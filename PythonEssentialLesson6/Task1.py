"""Даны две строки. Выведите на экран символы, которые есть в обоих строках."""

s1 = 'hello'
s2 = 'world'
s = list()

for i in s1:
    if i in s2:
        s.append(i)

print(*set(s))

print(*set(i for i in 'hello') & set(i for i in 'world'))

first_string = input('First string: ')
second_string = input('Second string: ')
common = set(first_string) & set(second_string)
print('Found', len(common), 'common characters:', *common)

