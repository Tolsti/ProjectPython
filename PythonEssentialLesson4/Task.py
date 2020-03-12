"""Напишите функцию-генератор для получения n первых простых чисел."""


def generator_prime_number(count):
    number_count = 2

    def prime_number(number):
        if number == 1:
            return False
        for i in range(2, number):
            if number % i == 0:
                return False
        return True

    while count != 0:
        if prime_number(number_count):
            yield number_count
            count -= 1
        number_count += 1


for i in generator_prime_number(200):
    print(i)
