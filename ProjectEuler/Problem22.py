"""Используйте names.txt (щелкнуть правой кнопкой мыши и выбрать 'Save Link/Target As...'),
текстовый файл размером 46 КБ, содержащий более пяти тысяч имен. Начните с сортировки в алфавитном порядке.
Затем подсчитайте алфавитные значения каждого имени и умножьте это значение на порядковый номер имени
в отсортированном списке для получения количества очков имени.
Например, если список отсортирован по алфавиту, имя COLIN (алфавитное значение которого 3 + 15 + 12 + 9 + 14 = 53)
является 938-ым в списке. Поэтому, имя COLIN получает 938 × 53 = 49714 очков.
Какова сумма очков имен в файле?"""

all_points = 0

abc = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5,
       'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
       'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15,
       'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
       'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

with open('p022_names.txt')as file:
    file = file.readline().replace('"', '')
    name_list = file.split(',')
    name_list.sort()

for i in range(len(name_list)):
    sum_of_letters = 0
    for j in range(len(name_list[i])):
        if name_list[i][j] in abc:
            sum_of_letters += abc[name_list[i][j]]
    # print(i + 1, name_list[i], sum_of_letters)
    all_points += sum_of_letters * (i + 1)
    # print(all_points)
print('Сумма очков имен в файле:', all_points)
