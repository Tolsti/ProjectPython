"""Напишите итератор, который возвращает элементы заданного списка в обратном порядке (аналог reversed)."""


class Reversed_Iterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

    def __iter__(self):
        return self


lst = [1, 2, 'True', 6, 23, 1, 78]
for i in lst:
    print(i, end=' ')
print()
for i in Reversed_Iterator(lst):
    print(i, end=' ')
