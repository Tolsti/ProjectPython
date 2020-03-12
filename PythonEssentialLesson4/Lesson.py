# values = [1, 2, 3, 4, 5]
#
# print(values[2])
# print(values.__getitem__(2))
# print()
#
# it = iter(values)
# print(it)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# # print(next(it))
# print()
#
# # how the for cycle works
# it = iter(values)
# while True:
#     try:
#         value = next(it)
#         print(value)
#     except StopIteration:
#         break

# # function my_for
# def my_for(iterable, callback):
#     it = iter(iterable)
#     while True:
#         try:
#             value = next(it)
#             callback(value)
#         except StopIteration:
#             break
#
#
# def loop_body(value):
#     print('Next value received:', value)
#
#
# my_for(range(10), loop_body)

# class SimpleIterable:
#     def __getitem__(self, item):
#         if 0 <= item <= 5:
#             return item * 2
#         else:
#             raise IndexError
#
#
# iterable = SimpleIterable()
# for value in iterable:
#     print(value)

# import math
#
#
# class MyRange:
#     def __init__(self, first, second=None, step=1):
#         if second is None:
#             self.start = 0
#             self.end = first
#         else:
#             self.start = first
#             self.end = second
#
#         if step != 0:
#             self.step = step
#         else:
#             raise ValueError('Step cannot be zero')
#
#         self.length = math.ceil((self.end - self.start) / self.step)
#
#     def __len__(self):
#         return self.length
#
#     def __getitem__(self, item):
#         if 0 <= item < len(self):
#             return self.start + item * self.step
#         else:
#             raise IndexError('MyRange index out of range')
#
#     def __repr__(self):
#         return 'MyRange({}, {}, {})'.format(self.start, self.end, self.step)
#
#     def __iter__(self):
#         return RangeIterator(self)
#
#
# class RangeIterator:
#     def __init__(self, range_instance):
#         self.range = range_instance
#         self.next_value = range_instance.start
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.next_value >= self.range.end and self.range.step > 0 or \
#                 self.next_value <= self.range.end and self.range.step < 0:
#             raise StopIteration
#
#         result = self.next_value
#         self.next_value += self.range.step
#
#         return result
#
#
# r = MyRange(10)
# it = iter(r)
# # print(next(it))
# # print(next(it))
# # print(next(it))
#
# for i in r:
#     print(i, end=' ')
# print()
# for i in MyRange(3, 8):
#     print(i, end=' ')
# print()
# for i in MyRange(3, 8, 2):
#     print(i, end=' ')
# print()
# for i in MyRange(10, 0, -1):
#     print(i, end=' ')
# print()
# print(len(MyRange(10)))
# print(r)
#
# r = MyRange(5)
# it = iter(r)
# print(r)
# print(it)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# for i in r:
#     print(i, end=' ')
# print()

# class List:
#     class _Node:
#         __slots__ = ('value', 'next')
#
#         def __init__(self, value, next=None):
#             self.value = value
#             self.next = next
#
#     class _NodeIterator:
#         def __init__(self, first):
#             self._next_node = first
#
#         def __iter__(self):
#             return self
#
#         def __next__(self):
#             if self._next_node is None:
#                 raise StopIteration
#
#             value = self._next_node.value
#             self._next_node = self._next_node.next
#
#             return value
#
#     def __init__(self, iterable=None):
#         self._head = None
#         self._tail = None
#         self._length = 0
#
#         if iterable is not None:
#             self.extend(iterable)
#
#     def append(self, value):
#         node = List._Node(value)
#
#         if len(self) == 0:
#             self._head = self._tail = node
#         else:
#             self._tail.next = node
#             self._tail = node
#
#         self._length += 1
#
#     def extend(self, iterable):
#         for value in iterable:
#             self.append(value)
#
#     def __len__(self):
#         return self._length
#
#     def __getitem__(self, item):
#         if item < 0:
#             item += len(self)
#
#         if not 0 <= item < len(self):
#             raise IndexError('list index out of range')
#
#         node = self._head
#         for _ in range(item):
#             node = node.next
#
#         return node.value
#
#     def __iter__(self):
#         return List._NodeIterator(self._head)
#
#
# # values = List([4, 2, 1, 8])
# # print(values)
# # print(values[0])
# # print(values[1])
# # print(values[-1])
# # for i in values:
# #     print(i, end=' ')
# # print()
# #
# # values = List([5, 1, 8, 3, 2, 0, 5])
# # for i in values:
# #     print(i, end=' ')
#
# if __name__ == '__main__':
#     for i in List(range(100000)):
#         if i % 1000 == 0:
#             print(i)

# def generator():
#     yield 'hello'
#     yield 'world'
#
#
# print(generator)
# print(generator())
#
# g = generator()

# def fibonacci(count):
#     first, second = 0, 1
#     for _ in range(count):
#         yield second
#         first, second = second, first + second
#
#
# # f = fibonacci(5)
# #
# # print(next(f))
# # print(next(f))
# # print(next(f))
# # print(next(f))
# # print(next(f))
# # print(next(f))
#
# count=int(input('How many Fibonacci numbers to print?'))
# for fib in fibonacci(count):
#     print(fib)

# import math
#
#
# class MyRange:
#     def __init__(self, first, second=None, step=1):
#         if second is None:
#             self.start = 0
#             self.end = first
#         else:
#             self.start = first
#             self.end = second
#
#         if step != 0:
#             self.step = step
#         else:
#             raise ValueError('Step cannot be zero')
#
#         self.length = math.ceil((self.end - self.start) / self.step)
#
#     def __len__(self):
#         return self.length
#
#     def __getitem__(self, item):
#         if 0 <= item < len(self):
#             return self.start + item * self.step
#         else:
#             raise IndexError('MyRange index out of range')
#
#     def __repr__(self):
#         return 'MyRange({}, {}, {})'.format(self.start, self.end, self.step)
#
#     def __iter__(self):
#         current = self.start
#         for _ in range(len(self)):
#             yield current
#             current += self.step
#
#
# for i in MyRange(5):
#     print(i)

# def generator_function():
#     for x in range(5):
#         for y in range(3):
#             if (x + y) % 2 == 0:
#                 yield x * y
#
#
# # эквивалент генератора функции выше
# generator2 = (x * y for x in range(5) for y in range(3) if (x + y) % 2 == 0)
# generator1 = generator_function()
# for value in generator1:
#     print(value, end=' ')
# print()
#
# for value in generator2:
#     print(value, end=' ')
# print()
#
# print(sum(x ** 2 for x in range(10)))

def subgenerator():
    yield '[subgenerator] hello'
    yield '[subgenerator] world'


def generator():
    yield from range(10)
    print()
    yield from (x * 3 for x in range(5))
    print()
    yield from subgenerator()
    yield 'end'


for value in generator():
    print(value)
