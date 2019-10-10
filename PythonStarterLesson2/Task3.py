a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите 4c: "))
d = pow(b, 2) - (4 * a * c)
if d > 0:
    print("Корни уравнения равны: ")
    print("x1 = ", (-1 * b + pow(d, 0.5)) / (2 * a))
    print("x2 = ", (-1 * b - pow(d, 0.5)) / (2 * a))
elif d == 0:
    print("Корень уравнения равен: ", -1 * b / (2 * a))
else:
    print("Нет решений.")