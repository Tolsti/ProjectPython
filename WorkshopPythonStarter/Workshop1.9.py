# Создайте переменную x и присвойте ей значение - -234.636
# Создайте переменную n1 в которой будет находится модуль числа x.
# Создайте переменную n2 в которой будет находится результат округления n1 с точностью до 2 знаков после запятой.
# Создайте переменную n3 в которую поместите переменную n2 преобразованную к целому типу.
# Создайте переменную n4 в которую будет помещен результат возведения n3 в квадрат. Используйте встроенные функции.
x = -234.636
n1 = abs(x)
n2 = round(n1, 2)
n3 = int(n2)
n4 = pow(n3, 2)

print(x)
print(n1)
print(n2)
print(n3)
print(n4)