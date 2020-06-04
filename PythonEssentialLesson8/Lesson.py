# import os.path
#
# filename = os.path.join('data', 'example1.txt')
# example_file = open(filename)
# print(example_file.read())
# example_file.close()


# * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * #


# import sys
#
#
# class MyManager(object):
#     def __init__(self):
#         self.resource = 42
#
#     def __enter__(self):
#         print('Entered context')
#         return self.resource
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('Left context')
#         if exc_val:
#             print('Exception occurred: {}'.format(exc_type))
#
#
# # with MyManager() as resource:
# #     print('Some actions with resource:', resource)
# # print()
# #
# # with MyManager() as resource:
# #     print('Some actions with resource:', resource)
# #     raise ValueError
#
#
# def my_with(manager, context_body):
#     resource = manager.__enter__()
#     exc_type, exc_value, exc_traceback = None, None, None
#     error = None
#     try:
#         context_body(resource)
#     except Exception as e:
#         exc_type, exc_value, exc_traceback = sys.exc_info()
#         error = e
#     finally:
#         manager.__exit__(exc_type, exc_value, exc_traceback)
#         if error:
#             raise error
#
#
# def context_body(resource):
#     print('Some actions with resource:', resource)
#     # raise ValueError
#
#
# my_with(MyManager(), context_body)


# * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * #


# with open('data/example1.txt')as file:
#     print(file.read())


# * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * #


# with open(__file__) as source:
#     for number, line in enumerate(source, 1):
#         print('{:3}| {}'.format(number, line), end='')


# * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * #


# filename = 'data/example2.txt'
#
# with open(filename) as data:
#     lines = data.readlines()
#
# lines.insert(1, 'insert line\n')
#
# with open(filename, 'w') as data:
#     data.writelines(lines)


# * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * #


# import datetime
# import statistics
#
# message_fmt = '''\
# # Статистика от: {date}
# # Количество:    {count}
# # Сумма:         {sum}
# # Среднее:       {mean}
# # Медиана:       {median}
# '''
#
# with open('data/Example3.txt', 'r+') as data:
#     numbers = [float(line) for line in data
#                if line != '\n' and not line.startswith('#')]
#
#     message = message_fmt.format(date=datetime.datetime.now(),
#                                  count=len(numbers),
#                                  sum=sum(numbers),
#                                  mean=statistics.mean(numbers),
#                                  median=statistics.median(numbers))
#
#     print(message, file=data)


# * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * #


# import io
#
# data = io.StringIO('asdf in memory')
# print(data.getvalue())
# print(data.tell())
# print(len(data.getvalue()))
# print(data.read())
# print(data.tell())
# print(data.read())
# print(data.seek(0))
# print(data.write('data'))
# print(data.tell())
# print(data.read())
# print(data.getvalue())


# * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * #


# import array
# import random
#
# numbers = [random.randint(-1000000000, 1000000000)
#            for _ in range(1000)]
#
# with open('data/example4.txt', 'w') as text_file:
#     for number in numbers:
#         text_file.write('{}\n'.format(number))
#
# numbers_array = array.array('i', numbers)
#
# with open('data/example4.bin', 'wb')as binary_file:
#     binary_file.write(numbers_array)


# * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * #


# numbers = []
# with open('data/example4.txt') as text_file:
#     # numbers = [int(line) for line in text_file]
#     for line in text_file:
#         numbers.append(int(line))
# print(*numbers)


# * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * #


# import array
# import os.path
#
# filename = 'data/example4.bin'
# filesize = os.path.getsize(filename)
# count = filesize // array.array('i').itemsize
# numbers = array.array('i', (0 for _ in range(count)))
#
# with open(filename,'rb')as binary_file:
#     binary_file.readinto(numbers)
# print(*numbers.tolist())


# * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * #


# import json
#
# users = [
#     {'username': 'John',
#      'email': 'john@hotmail.com'},
#     {'username': 'Linda',
#      'email': 'li23@gmail.com'},
#     {'username': 'Mario',
#      'email': 'mariobreaker@gmail.com'}
#     ]
#
# with open('data/example5.json', 'w') as file:
#     json.dump(users, file, indent=2)
#
# with open('data/example5.json') as data:
#     users = json.load(data)
# print(users)


# * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * #


# import json
#
#
# class User(object):
#     def __init__(self, name, email):
#         self.username = name
#         self.email = email
#
#     def to_json(self):
#         return {'username': self.username, 'email': self.email}
#
#     @classmethod
#     def from_json(cls, js_object):
#         return cls(js_object['username'], js_object['email'])
#
#     def __repr__(self):
#         return 'User({!r}, {!r})'.format(self.username, self.email)
#
#
# users = [User('Max', 'maximus@hotmail.com'),
#          User('Rita', 'ritka@mail.com'),
#          User('Nick', 'nikola@gmail.com')]
#
# with open('data/example5.json', 'w') as file:
#     json.dump(users, file, indent=2, default=User.to_json)
#
# with open('data/example5.json') as data:
#     users_json = json.load(data, object_hook=User.from_json)
# print(users_json)


# * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * #


# import json
#
# print(json.dumps({'first_field': True, 'second_field': None}))
# print(json.loads(json.dumps({'first_field': True, 'second_field': None})))


# * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * #


# import pickle
# import reprlib
#
#
# class Person(object):
#     def __init__(self, name, age, siblings=None):
#         self.name = name
#         self.age = age
#         self.siblings = siblings or []
#
#     @reprlib.recursive_repr()
#     def __repr__(self):
#         return 'Person({name!r}, {age!r}, {siblings!r})'.format_map(self.__dict__)
#
#     @staticmethod
#     def make_siblings(first, second):
#         first.siblings.append(second)
#         second.siblings.append(first)
#
#
# john = Person('John', 29)
# melissa = Person('Melissa', 24)
# Person.make_siblings(john, melissa)
#
# print(john, melissa)
#
# with open('data/example6.pkl', 'wb') as data:
#     pickle.dump((john, melissa), data)
#
# with open('data/example6.pkl', 'rb') as data:
#     print(*pickle.load(data))


# * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * #


# import pickle
#
# print(pickle.dumps({'first_field': True, 'second_field': None}))
# print(pickle.loads(pickle.dumps({'first_field': True, 'second_field': None})))
