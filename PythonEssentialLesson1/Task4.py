"""Ознакомьтесь со специальными методами в Python, используя ссылки в конце урока, и научитесь использовать те из них,
назначение которых вы можете понять. Возвращайтесь к этой теме на протяжении всего курса и изучайте специальные методы,
соответствующие темам каждого урока."""
    # https://habr.com/ru/post/186608/


class MyClass:

    # __init__(self, [...) Инициализатор класса.Ему передаётся всё, с чем был вызван первоначальный конструктор
    # (так, например, если мы вызываем x = SomeClass(10, 'foo'), __init__ получит 10 и 'foo' в качестве аргументов.
    # __init__ почти повсеместно используется при определении классов.
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # __cmp__(self, other)
    # Самый базовый из методов сравнения. Он, в действительности, определяет поведение для всех операторов сравнения
    # (>, ==, !=, итд.), но не всегда так, как вам это нужно (например, если эквивалентность двух экземпляров
    # определяется по одному критерию, а то что один больше другого по какому-нибудь другому). __
    # cmp__ должен вернуть отрицательное число, если self < other, ноль, если self == other,
    # и положительное число в случае self > other. Но, обычно, лучше определить каждое сравнение,
    # которое вам нужно, чем определять их всех в __cmp__. Но __cmp__ может быть хорошим способом избежать
    # повторений и увеличить ясность, когда все необходимые сравнения оперерируют одним критерием.
    def __cmp__(self, other):
        pass

    # __eq__(self, other)
    # Определяет поведение оператора равенства, ==.
    def __eq__(self, other):
        return len(self.name) == len(other.month) and self.age == other.age

    # __ne__(self, other)
    # Определяет поведение оператора неравенства, !=.
    def __ne__(self, other):
        return len(self.name) != len(other.month) and self.age != other.age

    # __lt__(self, other)
    # Определяет поведение оператора меньше, <.
    def __lt__(self, other):
        return len(self.name) < len(other.month)

    # __gt__(self, other)
    # Определяет поведение оператора больше, >.
    def __gt__(self, other):
        return self.age > other.age

    # __le__(self, other)
    # Определяет поведение оператора меньше или равно, <=.
    # __ge__(self, other)
    # Определяет поведение оператора больше или равно, >=.

