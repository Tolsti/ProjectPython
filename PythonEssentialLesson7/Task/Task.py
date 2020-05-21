"""Создайте модуль для получения простых чисел. Импортируйте его из другого модуля. Импортируйте отдельные его имена."""

import prime_module as prime
from prime_module import is_prime

for i in range(100):
    if is_prime(i) and i:
        print(i, end = ' ')
print()

print(*prime.list_of_prime(100))
