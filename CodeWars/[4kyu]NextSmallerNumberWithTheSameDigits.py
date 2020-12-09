def next_smaller(number):
    number, count = list(str(number)), len(str(number)) - 1
    
    for i in range(count - 1, -1, -1):
        for j in range(count, i - 1, -1):
            if number[j] < number[i]:
                number[j], number[i] = number[i], number[j]
                first, second = number[0:i + 1], number[-1:i:-1]
                if int(first[0]) != 0:
                    return int(''.join(first + second))
    return -1


print(next_smaller(907), 790)
print(next_smaller(531), 513)
print(next_smaller(135), -1)
print(next_smaller(2071), 2017)
print(next_smaller(414), 144)
print(next_smaller(123456798), 123456789)
print(next_smaller(123456789), -1)
print(next_smaller(1234567908), 1234567890)
print(next_smaller(123 ** 123))
print(next_smaller(30))
