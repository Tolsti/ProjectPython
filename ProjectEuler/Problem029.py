"""Рассмотрим все целочисленные комбинации ab для 2 ≤ a ≤ 5 и 2 ≤ b ≤ 5:

2**2=4, 2**3=8, 2**4=16, 2**5=32
3**2=9, 3**3=27, 3**4=81, 3**5=243
4**2=16, 4**3=64, 4**4=256, 4**5=1024
5**2=25, 5**3=125, 5**4=625, 5**5=3125
Если их расположить в порядке возрастания, исключив повторения,
мы получим следующую последовательность из 15 различных членов:

4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125

Сколько различных членов имеет последовательность ab для 2 ≤ a ≤ 100 и 2 ≤ b ≤ 100?"""


def integer_combinations_of_a_b(data_a, data_b):
    number_list = list()
    for a in range(2, data_a + 1):
        for b in range(2, data_b + 1):
            number_list.append(pow(a, b))

    return sorted(list(set(number_list)))


def main():
    print(len(integer_combinations_of_a_b(5, 5)), integer_combinations_of_a_b(5, 5))
    print(len(integer_combinations_of_a_b(100, 100)), integer_combinations_of_a_b(100, 100))


if __name__ == '__main__':
    main()
