"""Перепишите решение первого задания с помощью генератора."""


def reversed_generator(data):
    index = len(data)
    while index != 0:
        if index == 0:
            raise StopIteration
        index -= 1
        yield data[index]


lst = [1, 2, 'True', 6, 23, 1, 78]
for i in lst:
    print(i, end=' ')
print()
for i in reversed_generator(lst):
    print(i, end=' ')
