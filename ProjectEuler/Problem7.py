"""Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13. Очевидно, что 6-ое простое число - 13.
Какое число является 10001-ым простым числом?"""
# Долго считает, нужна оптимитизатия

prime = [i for i in range(2, 1000000)]
prime_list = list()
prime_tmp = list()
flag = 0
a = 0
while flag < 10001:
    prime_list.append(prime[0])
    prime_tmp = [i for i in prime if i % prime[0] != 0]
    prime = prime_tmp
    flag += 1
print(prime_list)
