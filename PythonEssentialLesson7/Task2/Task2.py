"""Повторите информацию о рассмотренных на уроке стандартных модулях.
Ознакомьтесь также с модулями calendar, heapq, bisect, array, enum."""

# import calendar
#
# c = calendar.TextCalendar(calendar.SUNDAY)
# show_month = c.formatmonth(2025, 1)
# print(show_month)
#
# show_month = calendar.TextCalendar(calendar.THURSDAY).formatmonth(2025, 1)
# print(show_month)
#
# hc = calendar.HTMLCalendar(calendar.THURSDAY).formatmonth(2025, 1)
# print(hc)
#
# c = calendar.TextCalendar(calendar.THURSDAY)
# for i in c.itermonthdays(2025, 4):
#     print(i, end=' ')
# print()
#
# for month in calendar.month_name:
#     print(month, end=' ')
# print()
#
# for day in calendar.day_name:
#     print(day, end=' ')
# print()
#
# for month in range(1, 13):
#     my_cal = calendar.monthcalendar(2025, month)
#     week1 = my_cal[0]
#     week2 = my_cal[1]
#
#     if week1[calendar.MONDAY] != 0:
#         audit_day = week1[calendar.MONDAY]
#     else:
#         audit_day = week2[calendar.MONDAY]
#
#     print('%10s %2d' % (calendar.month_name[month], auditday))


# * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * #


# import heapq
# import random
#
# # heappush()
# init_list = list(range(10, 99, 10))
# print(*init_list)
# random.shuffle(init_list)
# print(*init_list)
# heap = []
# [heapq.heappush(heap, x) for x in init_list]
# print(*heap)
# heapq.heappush(heap, 1)
# print(*heap)
# print()
#
# # heappop()
# out = heapq.heappop(heap)
# print(*heap)
# print(out)
# out = heapq.heappop(heap)
# print(*heap)
# print(out)
# out = heapq.heappop(heap)
# print(*heap)
# print(out)
# print()
#
# # heappushpop()
# new_item = 99
# out = heapq.heappushpop(heap, new_item)
# print(new_item)
# print(out)
# print(*heap)
# new_item = 999
# out = heapq.heappushpop(heap, new_item)
# print(new_item)
# print(out)
# print(*heap)
# print()
#
# # heapify()
# heap = [78, 34, 78, 11, 45, 13, 99]
# print(*heap)
# heapq.heapify(heap)
# print(*heap)
# print()
#
# # heapreplace()
# heap = [78, 34, 78, 11, 45, 13, 99]
# heapq.heapify(heap)
# print(*heap)
# heapq.heapreplace(heap, 12)
# print(*heap)
# heapq.heapreplace(heap, 100)
# print(*heap)
# print()
#
# # nlargest()
# heap = [78, 34, 78, 11, 45, 13, 99]
# heapq.heapify(heap)
# print(*heap)
# out = heapq.nlargest(2, heap)
# print(out)
# print()
#
# # nsmallest()
# heap = [78, 34, 78, 11, 45, 13, 99]
# heapq.heapify(heap)
# print(heap)
# out = heapq.nsmallest(2, heap)
# print(out)


# * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * #


# import bisect
#
#
# def contains(list_, elem):
#     index = bisect.bisect_left(list_, elem)
#     if index < len(list_):
#         return list_[index] == elem
#     return False
#
#
# print(contains(list(range(1000)), -10))
# print(contains([1, 2, 3, 6, 8, 10, 15], 10))
# print(contains([1, 2, 3, 6, 8, 10, 15], 0))
# print(contains([1, 2, 3, 6, 8, 10, 15], 20))


# * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * #


# import array
#
# arr = array.array('d', [1, 3.5, 4.5])
# print(arr)
# print()
#
# arr = array.array('i', [2, 4, 6, 8])
# print(arr)
# print(arr[0])
# print(arr[1])
# print(arr[-1])
# print()
#
# number_list = [2, 5, 62, 5, 42, 52, 48, 5]
# number_array = array.array('i', number_list)
# print(number_array[2:5])
# print(number_array[:-5])
# print(number_array[5:])
# print(number_array[:])
# print()
#
# numbers = array.array('i', [1, 2, 3, 5, 7, 10])
# print(numbers)
# numbers[0] = 0
# print(numbers)
# numbers[2:5] = array.array('i', [4, 6, 8])
# print(numbers)
# print()
#
# numbers = array.array('i', [1, 2, 3])
# print(numbers)
# numbers.append(4)
# print(numbers)
# numbers.extend([5, 6, 7])
# print(numbers)
# print()
#
# odd = array.array('i', [1, 3, 5])
# print(odd)
# even = array.array('i', [2, 4, 6])
# print(even)
# numbers = odd + even
# print(numbers)
# print()
#
# numbers=array.array('i',[1,2,3,3,4])
# print(numbers)
# del numbers[2]
# print(numbers)
# print()
#
# numbers=array.array('i',[10, 11, 12, 12, 13])
# print(numbers)
# numbers.remove(12)
# print(numbers)
# print(numbers.pop(2))
# print(numbers)


# * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * #


# import enum
#
#
# class Sequences(enum.Enum):
#     list = 1
#     tuple = 2
#     dict = 3
#
#
# print(Sequences.list)
# print(Sequences.tuple.name)
# print(Sequences.dict.value)
# print()
#
#
# class Sequences(enum.Enum):
#     list = enum.auto()
#     tuple = enum.auto()
#     dict = enum.auto()
#
#
# print(Sequences.list.value)
# print(Sequences.tuple.value)
# print(Sequences.dict.value)
# print()
#
#
# class Num(enum.Enum):
#     one = 1
#     two = 2
#     three = 3
#
#
# for n in Num:
#     print(n)
# print()
#
#
# class Color(enum.Enum):
#     BLUE = 1
#     BLACK = 2
#     BROWN = 3
#
#
# apples = {}
# apples[Color.BLUE] = 'blue'
# apples[Color.BLACK] = 'black'
# print(apples)
# print()
#
#
# class Students(enum.Enum):
#     IGOR = 1
#     SERGEY = 2
#     VASYA = 3
#
#     def info(self):
#         print('Name - %s, Value - %s' % (self.name, self.value))
#
#
# Students.IGOR.info()
