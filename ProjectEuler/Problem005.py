"""2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.
Какое самое маленькое число делится нацело на все числа от 1 до 20?"""
import time

timer1 = time.time()

for i in range(0, 1000000000, 20):
    if all([i % n == 0 for n in range(1, 21)]) and i != 0:
        print(i)
        break

timer2 = time.time()
print(timer2 - timer1)

# for i in range(1, 1000000000):
#     if i % 1 == 0 and i % 2 == 0 and i % 3 == 0 and i % 4 == 0 and i % 5 == 0 \
#             and i % 6 == 0 and i % 7 == 0 and i % 8 == 0 and i % 9 == 0 and i % 10 == 0:
#         print(i)
#         break
# for i in range(1, 1000000000):
#     if all([i % 2 == 0, i % 3 == 0, i % 4 == 0, i % 5 == 0, i % 6 == 0, i % 7 == 0, i % 8 == 0, i % 9 == 0,
#             i % 10 == 0, i % 11 == 0, i % 12 == 0, i % 13 == 0, i % 14 == 0, i % 15 == 0, i % 16 == 0, i % 17 == 0,
#             i % 18 == 0, i % 19 == 0, i % 20 == 0]):
#         print(i)
#         break
