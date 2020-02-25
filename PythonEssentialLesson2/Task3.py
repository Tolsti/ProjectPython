"""Создайте иерархию классов с использованием множественного наследования.
Выведите на экран порядок разрешения методов для каждого из классов. Объясните,
почему линеаризации данных классов выглядят именно так."""


class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


class E:
    pass


class F(D, E):
    pass


if __name__ == '__main__':
    print('Order of allowed methods of class A:')
    for i in A.mro():
        print(i)
    print('\nOrder of allowed methods of class B:')
    for i in B.mro():
        print(i)
    print('\nOrder of allowed methods of class C:')
    for i in C.mro():
        print(i)
    print('\nOrder of allowed methods of class D:')
    for i in D.mro():
        print(i)
    print('\nOrder of allowed methods of class E:')
    for i in E.mro():
        print(i)
    print('\nOrder of allowed methods of class F:')
    for i in F.mro():
        print(i)
