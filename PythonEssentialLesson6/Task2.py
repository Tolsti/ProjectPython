"""Создайте программу, которая эмулирует работу сервиса по сокращению ссылок.
Должна быть реализована возможность ввода изначальной ссылки и
короткого названия и получения изначальной ссылки по её названию."""

import random
import string

dictionary_links = dict()
links = ['vk.com', 'mail.ru', 'google.com', 'yandex.ru']


def abbreviated_link(url):
    abbreviated_url = 'link.com/' + \
                      ''.join(random.choice(string.ascii_letters + string.digits) for a in range(4))
    return abbreviated_url


for link in links:
    dictionary_links[link] = abbreviated_link(link)

while True:
    for i in dictionary_links:
        print(i, dictionary_links[i])

    print()
    print('A program that emulates the work of the link reduction service.')
    print(1, 'create an abbreviated link.')
    print(2, 'output a link.')
    print(3, 'exit.')

    flag = input('Select action: ')
    if flag in ['1', 'create', 'new']:
        create_link = input('The name of the link: ')
        dictionary_links[create_link] = abbreviated_link(create_link)
    elif flag in ['2', 'get', 'output']:
        get_link = input('The name of the link: ')
        try:
            print(dictionary_links[get_link])
        except KeyError:
            flag_on_the_existence_of_links = True
            for link in dictionary_links:
                if get_link == dictionary_links[link]:
                    print(link)
                    flag_on_the_existence_of_links = False
            if flag_on_the_existence_of_links:
                print('There is no such link')
    elif flag in ['3', 'exit', 'quit', 'q']:
        break

    print()
