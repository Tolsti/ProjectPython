"""Единичная дробь имеет 1 в числителе.
Десятичные представления единичных дробей со знаменателями от 2 до 10 даны ниже:

1/2	=	0.5
1/3	=	0.(3)
1/4	=	0.25
1/5	=	0.2
1/6	=	0.1(6)
1/7	=	0.(142857)
1/8	=	0.125
1/9	=	0.(1)
1/10	=	0.1
Где 0.1(6) значит 0.166666..., и имеет повторяющуюся последовательность из одной цифры.
Заметим, что 1/7 имеет повторяющуюся последовательность из 6 цифр.

Найдите значение d < 1000, для которого 1/d в десятичном виде содержит самую длинную
повторяющуюся последовательность цифр."""


def decimal_representations_of_unit_fractions():
    flt = str(1 / 7)[2:]
    tmp = ''
    count = 0

        


if __name__ == '__main__':

    num = longest = 1
    for n in range(3, 1000, 2):
        if n % 5 == 0:
            continue
    
        p = 1
        while (10 ** p) % n != 1:
            p += 1
    
        if p > longest:
            num, longest = n, p
    print(longest)
    print(num)
    decimal_representations_of_unit_fractions()

print(1/983)
import fractions

print(fractions.Fraction(1,7))