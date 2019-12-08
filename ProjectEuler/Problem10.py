"""Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.
Найдите сумму всех простых чисел меньше двух миллионов."""

arr = list(range(2000001))
for i in arr[2:]:
    for j in range(i + i, len(arr), i):
        arr[j] = 0
print(arr)
print(sum([i for i in arr if not (i == 0 or i == 1)]))
