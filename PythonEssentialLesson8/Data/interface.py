def generalized_interface(list_links=None):
    if list_links is None:
        print('No short links.')
    else:
        for key, value in zip(list_links, list_links.values()):
            len_ = 2 + max(len(key), len(value))
            print(' ' + ('-' * len_) + '  ', end='')
        print()
        for key, value in zip(list_links, list_links.values()):
            tab, flag = '', max(len(key), len(value)) - min(len(key), len(value))
            if len(value) > len(key):
                while flag > 0:
                    tab, flag = tab + ' ', flag - 1
            print('|', key, tab + '|', end=' ')
        print()
        for key, value in zip(list_links, list_links.values()):
            tab, flag = '', max(len(key), len(value)) - min(len(key), len(value))
            if len(key) > len(value):
                while flag > 0:
                    tab, flag = tab + ' ', flag - 1
            print('|', value, tab + '|', end=' ')
        print()
        for key, value in zip(list_links, list_links.values()):
            len_ = 2 + max(len(key), len(value))
            print(' ' + ('-' * len_) + '  ', end='')
        print()

    print(1, 'Create an abbreviated link.')
    print(2, 'Output a link.')
    print(3, 'Exit.')

    return input('Select action: ')
