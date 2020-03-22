"""Удивительно, но существует только три числа, которые могут быть записаны в виде суммы четвертых степеней их цифр:

1634 = 1**4 + 6**4 + 3**4 + 4**4
8208 = 8**4 + 2**4 + 0**4 + 8**4
9474 = 9**4 + 4**4 + 7**4 + 4**4
1 = 14 не считается, так как это - не сумма.

Сумма этих чисел равна 1634 + 8208 + 9474 = 19316.

Найдите сумму всех чисел, которые могут быть записаны в виде суммы пятых степеней их цифр."""
import time


def all_numbers_written_as_sum_powers(power):
    sum_degree = 0
    count = 2
    while count < 1000000:
        sum_number = 0
        for i in str(count):
            sum_number += int(i) ** power
        if count == sum_number:
            print(sum_number)
            sum_degree += sum_number

        count += 1
    return sum_degree


def all_numbers_written_as_sum_powers_version_2(power):
    dictionary_of_numbers_in_power = {1: pow(1, power), 2: pow(2, power), 3: pow(3, power), 4: pow(4, power),
                                      5: pow(5, power), 6: pow(6, power), 7: pow(7, power), 8: pow(8, power),
                                      9: pow(9, power), 0: pow(0, power)}
    sum_powers = 0

    for count in range(2, 1000000):
        sum_number = 0

        for i in str(count):
            sum_number += dictionary_of_numbers_in_power[int(i)]
        if count == sum_number:
            print(sum_number)
            sum_powers += sum_number

    return sum_powers


if __name__ == '__main__':
    time_start = time.time()
    print('The sum of all numbers that can be written as the sum of powers of their digits:',
          all_numbers_written_as_sum_powers(5))
    time_end = time.time()
    print(time_end - time_start)

    print()

    time_start = time.time()
    print('The sum of all numbers that can be written as the sum of powers of their digits:',
          all_numbers_written_as_sum_powers_version_2(5))
    time_end = time.time()
    print(time_end - time_start)
