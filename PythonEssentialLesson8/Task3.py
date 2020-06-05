"""Модифицируйте исходный код сервиса по сокращению ссылок из предыдущих двух уроков так,
чтобы он сохранял базу ссылок на диске и не «забывал» при перезапуске.
При желании можете ознакомиться с модулем shelve (https://docs.python.org/3/library/shelve.html),
который в данном случае будет весьма удобен и упростит выполнение задания. """

import Data.interface, Data.abbreviated
import shelve

print('Program that emulates the work of the key reduction service.')

while True:
    with shelve.open('data/list_of_links') as data:
        flag = Data.interface.generalized_interface(data)

        if flag in ['1', 'create', 'new']:
            create_link = input('Name of the link: ')
            data[create_link] = Data.abbreviated.abbreviated_link()
            print(create_link, '  has an abbreviated link  ', data[create_link])

        elif flag in ['2', 'get', 'output']:
            get_link = input('Name of the link: ')
            for key, value in zip(data, data.values()):
                if get_link not in data.values() and get_link not in data:
                    print('There is no such link.')
                    break
                elif key == get_link:
                    print(key, '  has an abbreviated link  ', value)
                elif value == get_link:
                    print(value, '  has a link  ', key)

        elif flag in ['del']:
            get_del_link = input('Name of the link to delete: ')
            for key in data:
                if get_del_link in [key, data[key]]:
                    del data[key]

        elif flag in ['3', 'exit', 'quit', 'q']:
            print()
            print(' ' * 5 + '#' * 7, ' ' * 5 + '#' + ' ' * 7 + '#', ' ' * 5 + '#', ' ' * 5 + '#' * 7)
            print(' ' * 5 + '#', ' ' * 13 + '#' + ' ' * 3 + '#', ' ' * 8, ' ' * 8 + '#')
            print(' ' * 5 + '#' * 5, ' ' * 11 + '#', ' ' * 9 + '#', ' ' * 8 + '#')
            print(' ' * 5 + '#', ' ' * 13 + '#' + ' ' * 3 + '#', ' ' * 7 + '#', ' ' * 8 + '#')
            print(' ' * 5 + '#' * 7, ' ' * 5 + '#' + ' ' * 7 + '#', ' ' * 5 + '#', ' ' * 8 + '#')
            # print()
            # print('#######     #       #     #     #######')
            # print('#             #   #                #   ')
            # print('#####           #         #        #   ')
            # print('#             #   #       #        #   ')
            # print('#######     #       #     #        #   ')
            break
