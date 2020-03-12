"""Взяв за основу код примера 06-iterable_with_an_iterator.py, расширьте функциональность класса MyList,
добавив методы для очистки списка, добавления элемента в произвольное место списка, удаления элемента из конца и
произвольного места списка."""


class MyList(object):
    """Класс списка"""

    class _ListNode(object):
        """Внутренний класс элемента списка"""

        # По умолчанию атрибуты-данные хранятся в словаре __dict__.
        # Если возможность динамически добавлять новые атрибуты
        # не требуется, можно заранее их описать, что более
        # эффективно с точки зрения памяти и быстродействия, что
        # особенно важно, когда создаётся множество экземляров
        # данного класса.
        __slots__ = ('value', 'prev', 'next')

        def __init__(self, value, prev=None, next=None):
            self.value = value
            self.prev = prev
            self.next = next

        def __repr__(self):
            return 'MyList._ListNode({}, {}, {})'.format(self.value, id(self.prev), id(self.next))

    class _Iterator(object):
        """Внутренний класс итератора"""

        def __init__(self, list_instance):
            self._list_instance = list_instance
            self._next_node = list_instance._head

        def __iter__(self):
            return self

        def __next__(self):
            if self._next_node is None:
                raise StopIteration

            value = self._next_node.value
            self._next_node = self._next_node.next

            return value

    def __init__(self, iterable=None):
        # Длина списка
        self._length = 0
        # Первый элемент списка
        self._head = None
        # Последний элемент списка
        self._tail = None
        # self.iterable = iterable

        # Добавление всех переданных элементов
        if iterable is not None:
            for element in iterable:
                self.append(element)

    def append(self, element):
        """Добавление элемента в конец списка"""

        # Создание элемента списка
        node = MyList._ListNode(element)

        if self._tail is None:
            # Список пока пустой
            self._head = self._tail = node
        else:
            # Добавление элемента
            self._tail.next = node
            node.prev = self._tail
            self._tail = node

        self._length += 1

    def insert(self, index, element):
        temp_list = MyList._Iterator(self)

        if temp_list is not None:
            self.clear()
            count = 0
            for i in temp_list:
                if count == index:
                    self.append(element)
                self.append(i)
                count += 1
            if index >= self._length:
                self.append(element)
        else:
            self.append(element)

    def pop(self, index=None):
        temp_list = MyList._Iterator(self)
        temp_len = self._length
        self.clear()
        count = 0
        if index is None:
            for i in temp_list:
                if count < temp_len - 1:
                    self.append(i)
                    count += 1
        else:
            if index >= temp_len:
                raise IndexError
            for i in temp_list:
                if count != index:
                    self.append(i)
                count += 1

    def clear(self):
        self._head = self._tail = None
        self._length = 0

    def __len__(self):
        return self._length

    def __repr__(self):
        # Метод join класса str принимает последовательность строк
        # и возвращает строку, в которой все элементы этой
        # последовательности соединены изначальной строкой.
        # Функция map применяет заданную функцию ко всем элементам
        # последовательности.
        return 'MyList([{}])'.format(', '.join(map(repr, self)))

    def __getitem__(self, index):
        if not 0 <= index < len(self):
            raise IndexError('list index out of range')

        node = self._head
        for _ in range(index):
            node = node.next

        return node.value

    def __iter__(self):
        return MyList._Iterator(self)


def main():
    # Создание списка
    my_list = MyList([1, 2, 5, 'True'])

    # Вывод длины списка
    print('Вывод длины списка:', len(my_list))

    # Вывод самого списка
    print('Вывод самого списка:', my_list)

    # Обход списка
    print('Обход списка: ', end='')
    for element in my_list:
        print(element, end=' ')
    print()

    # Добавить элемент в произвольное место в списке
    print('Добавить элемент в произвольное место в списке: ', end='')
    my_list.insert(2, 99)
    for element in my_list:
        print(element, end=' ')
    print()

    # Удалить последний элемент в списке
    print('Удалить последний элемент в списке: ', end='')
    my_list.pop()
    for element in my_list:
        print(element, end=' ')
    print()

    # Удалить элемент из списка по индексу
    print('Удалить элемент из списка по индексу: ', end='')
    my_list.pop(2)
    for element in my_list:
        print(element, end=' ')
    print()

    # Очистить список
    print('Очистить список: ', end=' ')
    my_list.clear()
    print(my_list, end=' ')
    print(len(my_list))
    for element in my_list:
        print(element, end=' ')
    print()


if __name__ == '__main__':
    main()
