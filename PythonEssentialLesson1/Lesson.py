# class MyObject:
#     int_field = 8
#     str_field = 'a string'
#
#
# print(MyObject.int_field)
# print(MyObject.str_field)
#
# object1 = MyObject()
# object2 = MyObject()
#
# print(object1.int_field)
# print(object2.str_field)
#
# MyObject.int_field = 10
# print(MyObject.int_field)
# print(object1.int_field)
#
# object1.str_field = 'another string'
# print(MyObject.str_field)
# print(object1.str_field)
# print(object2.str_field)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def print_info(self):
#         print(self.name, 'is', self.age)
#
#
# john = Person('John', 22)
# lucy = Person('Lucy', 21)
#
# # john = Person()
# # john.name = 'John'
# # john.age = 22
#
# # lucy = Person()
# # lucy.name = 'Lucy'
# # lucy.age = 21
#
# # print(john.name, 'is', john.age)
# # print(lucy.name, 'is', lucy.age)
#
# john.print_info()
# lucy.print_info()

# class MyObject:
#     class_attribute = 8
#
#     def __init__(self):
#         self.data_attribute = 42
#
#     def instance_method(self):
#         print(self.data_attribute)
#
#     @staticmethod
#     def static_method():
#         print(MyObject.class_attribute)
#
#
# if __name__ == '__main__':
#     MyObject.static_method()
#     obj = MyObject()
#     obj.instance_method()
#     obj.static_method()

# class Rectangle:
#     def __init__(self, side_a, side_b):
#         self.side_a = side_a
#         self.side_b = side_b
#
#     def __repr__(self):
#         return 'Rectangle(%.1i, %.1i)' % (self.side_a, self.side_b)
#
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def __repr__(self):
#         return 'Circle(%.1f)' % self.radius
#
#     @classmethod
#     def from_rectangle(cls, rectangle):
#         radius = (rectangle.side_a ** 2 + rectangle.side_b ** 2) ** 0.5 / 2
#         return cls(radius)
#
#
# def main():
#     rectangle = Rectangle(3, 4)
#     print(rectangle)
#
#     firs_circle = Circle(1)
#     print(firs_circle)
#
#     second_circle = Circle.from_rectangle(rectangle)
#     print(second_circle)
#
#
# if __name__ == '__main__':
#     main()

# class MyObject:
#     def __init__(self):
#         self.__private_attribute = 0
#
#     def get_attribute(self):
#         return self.__private_attribute
#
#     def set_attribute(self, value):
#         if value < 100:
#             self.__private_attribute = value
#
#
# obj = MyObject()
# obj.set_attribute(800)
# print(obj.get_attribute())
# obj.set_attribute(30)
# print(obj.get_attribute())

# class MyObject:
#     def __init__(self):
#         self.__attribute = 0
#
#     @property
#     def attribute(self):
#         return self.__attribute
#
#     @attribute.setter
#     def attribute(self, value):
#         if value < 100:
#             self.__attribute = value
#
#
# obj = MyObject()
# print(obj.attribute)
# obj.attribute = 30
# print(obj.attribute)
# obj.attribute = 900
# print(obj.attribute)

# class Complex:
#     def __init__(self, real=0.0, imaginary=0.0):
#         self.real = real
#         self.imaginary = imaginary
#
#     def __repr__(self):
#         return 'Complex({!r}, {!r})'.format(self.real, self.imaginary)
#
#     def __str__(self):
#         return '{}{:+d}i'.format(self.real, self.imaginary)
#
#     def __add__(self, other):
#         return Complex(self.real + other.real, self.imaginary + other.imaginary)
#
#     def __neg__(self):
#         return Complex(-self.real, -self.imaginary)
#
#     def __sub__(self, other):
#         return self + (-other)
#
#     def __abs__(self):
#         return (self.real ** 2 + self.imaginary ** 2) ** 0.5
#
#     def __eq__(self, other):
#         return self.real == other.real and self.imaginary == other.imaginary
#
#
# c = Complex(2, 5)
# print(c.__str__())
# print(c.__repr__())
# print((Complex(2, 3) + Complex(2, -1)).__repr__())
# print((Complex(2, 3) - Complex(1, 1)).__repr__())
# print(abs(Complex(2, 3)))

# class Singleton:
#     _instance = None
#
#     def __new__(cls):
#         if cls._instance is None:
#             cls._instance = object.__new__(cls)
#         return cls._instance
#
#     def __init__(self):
#         self.value = 'some value'

class MyObject:
    def __init__(self):
        self.password = None

    def __getattribute__(self, item):
        if item == 'secret_field' and self.password == '9ea)fc':
            return 'Secret value'
        else:
            return object.__getattribute__(self, item)

