"""module prime numbers"""


def is_prime(number):
    if number == 1:
        return False
    if number % 2 == 0:
        return number == 2
    tmp = 3
    while tmp ** 2 <= number and number % tmp != 0:
        tmp += 2
    return tmp ** 2 > number


def list_of_prime(rng):
    lst = list(range(rng))
    for i in lst[2:]:
        for j in range(i + i, len(lst), i):
            lst[j] = 0
    return [i for i in lst if i not in [0, 1]]


if __name__ == '__main__':
    for i in range(100):
        if is_prime(i) and i:
            print(i, end = ' ')
    print()
    
    print(*list_of_prime(100))
