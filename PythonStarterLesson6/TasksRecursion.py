"""Дано натуральное число n. Выведите все числа от 1 до n."""
import random

tmp_num = random.randint(1, 20)
print('n = ' + str(tmp_num))


def fun_rec1(a, b = 1):
    if b > a:
        print('\n')
        return 0
    else:
        print(b, end = ' ')
        return fun_rec1(a, b + 1)


fun_rec1(tmp_num)

'''Даны два целых числа A и В (каждое в отдельной строке).
Выведите все числа от A до B включительно, в порядке возрастания, если A < B,
или в порядке убывания в противном случае.'''
tmp_a = random.randint(-20, 20)
tmp_b = random.randint(-20, 20)
print('a = ' + str(tmp_a) + ', b = ' + str(tmp_b))

if tmp_a < tmp_b:
    def fun_rec2(a, b):
        if a <= b:
            print(a, end = ' ')
            return fun_rec2(a + 1, b)
        else:
            return 0
else:
    def fun_rec2(a, b):
        if b <= a:
            print(a, end = ' ')
            return fun_rec2(a - 1, b)
        else:
            return 0

fun_rec2(tmp_a, tmp_b)
