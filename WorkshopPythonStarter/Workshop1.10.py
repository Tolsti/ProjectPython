# Считаем, что библиотека math подключена.
# Создайте переменную PI и присвойте ей значение константы Pi из библиотеки math.
# Создайте переменную x и присвойте ей значение PI без дробной части, использую функцию библиотеки math.
# Создайте переменную y и присвойте ей значения синуса угла x, используя функцию библиотеки math.
import math
PI = math.pi
x = math.trunc(PI)
y = math.sin(x)
print(PI)
print(x)
print(y)