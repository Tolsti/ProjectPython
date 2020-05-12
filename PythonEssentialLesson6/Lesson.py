# print(hash('hello'))
# print(hash('world'))
# print(hash(False))
# print(hash((1, 2, 3)))
# print(hash(3.5))
# print(hash(42))
# # print(hash([2, 3, 4])) # изменяемый обьект не хэшируется


# * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * #


# print(set([1, 2, 3]))
# print(frozenset([1, 2, 3]))
# print({1, 2, 3})
# print({1, 2, 3, 3, 3, 2})
# print({i ** 2 for i in range(1, 11)})


# * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * #


# first_set = {5, 2, 1, 8, 3, 10}
# second_set = {1, 2, 3, 4, 5, 6, 10}
#
# print(first_set & second_set)
# print(second_set & first_set)
# print(first_set.intersection(second_set))
# print(second_set.intersection(first_set))
# print(first_set | second_set)
# print(first_set.union(second_set))
# print(first_set - second_set)
# print(second_set - first_set)
# print(first_set.difference(second_set))
# print(second_set.difference(first_set))
# print(first_set ^ second_set)
# print(first_set.symmetric_difference(second_set))
# # print(first_set | [1, 2, 3])  # так делать нельзя
# print(first_set.union([1, 2, 3, 14]))
# print({1, 2} < {1, 2, 3})
# print({1, 2, 3} <= {1, 2, 3})
# print({1, 2, 3}.issubset({1, 2, 3}))
#
# first_set.add(15)
# print(first_set)
#
# first_set.remove(5)  # если удалить не существующий элеиент, то будет ошибка
# print(first_set)
#
# first_set.discard(1)
# print(first_set)
#
# first_set.update(second_set)
# print(first_set)
# print(second_set)
#
# print(first_set.intersection(range(3, 8)))
#
# first_set &= {i for i in range(3, 8)}
# print(first_set)
#
# first_set.update({5, 2, 1, 10, 15, 12, 11})
# print(first_set)
#
# first_set.difference_update(second_set)
# print(first_set)
#
# print(first_set.isdisjoint(second_set))
#
# first_set.update(range(10, 15))
# print(first_set)
# print(second_set)
#
# first_set.symmetric_difference_update(second_set)
# print(first_set)
#
# print({1, 2, 3} == {3, 2, 1})
# print({1, 2, 3} == {1, 2, 5})
# print({1, 2, 3} == frozenset([1, 2, 3]))
# print({1, 2} in {frozenset([1]), frozenset([3, 2]), frozenset([2, 1])})
#
# print(set('asdf'))
# print({'hello', 'world'})
#
# # first_string = input('First string: ')
# # second_string = input('Second string: ')
# first_string = 'hello'
# second_string = 'world'
# common = set(first_string) & set(second_string)
# print('Found', len(common), 'common characters:', *common)
#
# vowels = {'a', 'o', 'u', 'i', 'e', 'y'}
# # string = input('Enter a string: ')
# string = 'hello'
# print(' '.join(vowels.intersection(string)))
#
# # words = input('Enter a string: ').split(', ')
# words = 'hello, world, word'.split(', ')
# for word in words:
#     vowels.intersection_update(word.lower())
# print(' '.join(vowels))


# * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * #


# dict_ = {'name': 'John', 'occupation': 'dentist', 'age': 32}
# print(dict_)
#
#
# def function(**kwargs):
#     print(kwargs)
#
#
# function(a=5, b=8, c=123)
#
#
# # function(3, 5)  # будет ошибка, это не позиционный объект
#
# def function(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
#
# function(2, 3, a=5)
#
# print(2, 3, sep=' --- ', end='\n-------\n')
# options = {
#     'sep': ' --- ',
#     'end': '\n-------\n'
# }
# print(2, 3, **options)


# * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * #


# print({'one': 1, 'two': 2, 'three': 3})
# print(dict(one=1, two=2, three=3))
# print(dict([('one', 1), ('two', 2), ('three', 3)]))


# * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * #


# phonebook = {'Guido': '832-43-18', 'Mary': '123-80-24'}
#
# print(len(phonebook))
# print('Guido' in phonebook)
# print(phonebook['Guido'])
# print('Ron' in phonebook)
# # print(phonebook['Ron'])  # нет такого значения, будет ошибка
# print(phonebook.get('Ron', '000-00-00'))  # если нет такого значения, то просто покажет это знвчение
# print(phonebook.get('Mary', '000-00-00'))
# print(phonebook)
# print(phonebook.setdefault('Ron', '000-00-00'))  # если нет такого значения, то добавит в словарь
# print(phonebook.setdefault('Mary', '000-00-00'))  # если есть в словоре, то ничего не изменит
# print(phonebook)
# phonebook['Ron'] = '123-45-19'
# print(phonebook)
# phonebook['Jack'] = '324-88-45'
# print(phonebook)
# del phonebook['Jack']
# print(phonebook)
# print(dict.fromkeys(['Mary', 'Jack', 'Linda'], '123-45-67'))
# ron = phonebook.pop('Ron')
# print(ron)
# print(phonebook)
# print(phonebook.popitem())
# print(phonebook)
# phonebook.update(Mary='348-45-76', Jack='127-43-77')
# print(phonebook)
# phonebook.update({'Alex': '456-27-48', 'Kate': '111-67-22'})
# print(phonebook)
# phonebook.update([('Michael', '456-45-86'), ('Linda', '777-24-86')])
# print(phonebook)
# phonebook.clear()
# print(phonebook)


# * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * #


# phonebook = {'Mary': '235-76-34', 'Kate': '678-65-43', 'Alex': '888-76-52', 'Nicholas': '289-34-35'}
# print(phonebook.keys())
# print(phonebook.values())
# print(phonebook.items())
#
# for name, number in phonebook.items():
#     print(name + '\'s number is', number)
# print()
#
# for name in phonebook.keys():
#     print(name)
# print()
#
# for name in phonebook:
#     print(name)
# print()
#
# for number in phonebook.values():
#     print(number)
# print()
#
# print(list(phonebook.keys()))
# print(iter(phonebook.keys()))
#
# people = phonebook.keys()
# print(people)
# phonebook['Linda'] = '666-76-34'
# print(phonebook)
# print(people)
# del phonebook['Linda']
# print(phonebook)
# print(people)
#
# print(people & {'Alex', 'Alexander', 'Mary', 'John'})
# first_phonebook = phonebook
# second_phonebook = {'George': '456-87-23', 'Victor': '123-45-89', 'Kate': '234-45-18'}
# print(first_phonebook.keys() & second_phonebook.keys())
