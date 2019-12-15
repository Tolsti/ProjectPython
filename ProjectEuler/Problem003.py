"""Простые делители числа 13195 - это 5, 7, 13 и 29.
Каков самый большой делитель числа 600851475143, являющийся простым числом?"""

prime = [i for i in range(2, 100000)]
prime_list = list()
prime_tmp = list()
flag = 0
a = 0
while flag < 1000:
    prime_list.append(prime[0])
    a = prime[0]
    prime_tmp = [i for i in prime if i % a != 0]
    prime = prime_tmp
    flag += 1

number = 600851475143
arr = [i for i in range(2, 1000000) if number % i == 0 and i in prime_list]
print(max(arr))
