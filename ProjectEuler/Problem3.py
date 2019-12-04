"""Простые делители числа 13195 - это 5, 7, 13 и 29.
Каков самый большой делитель числа 600851475143, являющийся простым числом?"""

number = 600851475143
flag = number - 1
while flag > 1:
    if number % flag == 0:
        print(flag)
    flag -= 1
# Список простых чисел
prime = [i for i in range(2, 10000)]
prime_list = list()
prime_tmp = list()
flag = 0
while flag < 100:
    prime_list.append(prime[0])
    prime_tmp = [i for i in prime if i % prime_list[flag] != 0]
    prime = prime_tmp
    flag += 1
print(prime_list)
