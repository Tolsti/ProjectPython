"""Создайте программу, которая проверяет, является ли палиндромом введённая фраза."""

tmp_str = 'А РОНО дети возле кафе "Факел" зовите донора.'


def fun_polindrom(a):
    a = a.lower()
    for i in [' ', ',', '.', ':', ';', '!', '?', '-', '\"', '\'']: a = a.replace(i, '')
    b = a[::-1]
    if a == b:
        return True
    else:
        return False


print('Является ли фраза полиндромом: ' + str(fun_polindrom(tmp_str)))
