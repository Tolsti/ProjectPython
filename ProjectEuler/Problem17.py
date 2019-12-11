"""Если записать числа от 1 до 5 английскими словами (one, two, three, four, five),
то используется всего 3 + 3 + 5 + 4 + 4 = 19 букв.
Сколько букв понадобится для записи всех чисел от 1 до 1000 (one thousand) включительно?
Примечание: Не считайте пробелы и дефисы. Например, число 342 (three hundred and forty-two) состоит из 23 букв,
число 115 (one hundred and fifteen) - из 20 букв.
Использование "and" при записи чисел соответствует правилам британского английского."""

dictionary = {
    1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
    6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
    11: 'eleven', 12: 'twelve', 13: 'thirteen',
    10: 'ten', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
    60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety',
    1000: 'one thousand'
}
for i in range(10, 1000):
    if 13 < i < 20:
        dictionary[i] = dictionary[i - 10] + 'teen'
    if (20 < i < 100) and i % 10 != 0:
        dictionary[i] = dictionary[int(i / 10) * 10] + ' ' + dictionary[i % 10]
    if i % 100 == 0:
        dictionary[i] = dictionary[int(i / 100)] + ' ' + 'hundred'
    if (100 < i < 1000) and i % 10 == 0 and i % 100 != 0:
        dictionary[i] = dictionary[int(i / 100)] + ' ' + 'hundred' + ' ' + dictionary[i % 100]
    if (100 < i < 1000) and i % 10 != 0 and i % 100 != 0:
        dictionary[i] = dictionary[int(i / 100)] + ' ' + 'hundred' + ' and ' + dictionary[i % 100]

result = ''
for i in range(1, 1001):
    print(dictionary[i])
    result += dictionary[i]
print(''.join(result.split()))
print(len(''.join(result.split())))
