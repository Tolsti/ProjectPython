"""Перепишите домашнее задание предыдущего урока (сервис для сокращения ссылок) таким образом,
чтобы у него была основная часть, которая отвечала бы за логику работы и предоставляла обобщённый интерфейс,
и модуль представления, который отвечал бы за взаимодействие с пользователем. При замене последнего на другой,
взаимодействующий с пользователем иным способом, программа должна продолжать корректно работать."""

import abbreviated
import interface

print('Program that emulates the work of the key reduction service.')

while True:
    links = abbreviated.dictionary_links
    flag = interface.generalized_interface(links)
    if flag in ['1', 'create', 'new']:
        create_link = input('The name of the link: ')
        links[create_link] = abbreviated.abbreviated_link()
        print(create_link, '  has an abbreviated link  ', links[create_link])
    elif flag in ['2', 'get', 'output']:
        get_link = input('The name of the link: ')
        for key, value in zip(links, links.values()):
            if get_link not in links.values() and get_link not in links:
                print('There is no such link.')
                break
            elif key == get_link:
                print(key, '  has an abbreviated link  ', value)
            elif value == get_link:
                print(value, '  has a link  ', key)
    
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
