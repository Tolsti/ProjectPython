# class Base:
#     def method(self):
#         print('Hello!!!')
#
#
# class Child(Base):
#     def child_method(self):
#         print('Hello from child method')
#
#     def method(self):
#         print('Hello from redefined method')
#
#
# obj = Child()
# obj.method()
# obj.child_method()

# class Figure:
#     def __init__(self, side=0.0):
#         self.side = side
#
#
# class Square(Figure):
#     def draw(self):
#         for i in range(self.side):
#             print('*  ' * self.side)
#
#
# class Triangle(Figure):
#     def draw(self):
#         for i in range(1, self.side + 1):
#             print('*  ' * i)
#
#
# def main():
#     square = Square(5)
#     triangle = Triangle(8)
#
#     square.draw()
#     print()
#     triangle.draw()
#
#
# if __name__ == '__main__':
#     main()

# class Horse:
#     def run(self):
#         print('I am running')
#
#
# class Bird:
#     def fly(self):
#         print('I am flying')
#
#
# class Pegasus(Horse, Bird):
#     pass
#
#
# def main():
#     pegasus = Pegasus()
#     pegasus.run()
#     pegasus.fly()
#
#
# if __name__ == '__main__':
#     main()

# class Base(object):
#     def method(self):
#         print('Method class:', __class__.__name__)
#         print('Instance class:', type(self).__name__)
#
#
# class Child(Base):
#     pass
#
#
# if __name__ == '__main__':
#     base_instance = Base()
#     base_instance.method()
#
#     child_instance = Child()
#     child_instance.method()

# class MethodContainer:
#     def __init__(self, data):
#         self.data = data
#
#     def method(self):
#         print('method invoked')
#         print('data = ', self.data)
#
#
# instance = MethodContainer(8)
# print(type(MethodContainer.method))
# print(type(instance.method))

# class Base:
#     def method(self):
#         print('Base method invoked on', type(self).__name__, 'instance')
#
#
# class Child(Base):
#     def method(self):
#         # Base.method(self)
#         # super(Child, self).method()
#         super().method()
#         print('Child method invoked on', type(self).__name__, 'instance')
#
#
# base_instance = Base()
# base_instance.method()
# print()
# child_instance = Child()
# child_instance.method()
# print()
# Base.method(child_instance)

# class Animal:
#     def __init__(self):
#         self.can_run = False
#         self.can_fly = False
#
#     def print_abilities(self):
#         print(type(self).__name__ + ':')
#         print('Can run:', self.can_run)
#         print('Can fly:', self.can_fly)
#         print()
#
#
# class Horse(Animal):
#     def __init__(self):
#         super().__init__()
#         self.can_run = True
#
#
# class Bird(Animal):
#     def __init__(self):
#         super().__init__()
#         self.can_fly = True
#
#
# class Pegasus(Horse, Bird):
#     pass
#
#
# if __name__ == '__main__':
#     horse = Horse()
#     horse.print_abilities()
#
#     bird = Bird()
#     bird.print_abilities()
#
#     pegasus = Pegasus()
#     pegasus.print_abilities()

# def check_instance(obj, cls):
#     return check_subclass(type(obj), cls)
#
#
# def check_subclass(child, base):
#     for direct_base in child.__bases__:
#         if child == base:
#             return True
#
#         if base == direct_base:
#             return True
#         return check_subclass(direct_base, base)
#
#     return False
#
#
# print('1: ', check_instance(8, int))
# print('2: ', check_instance(8, str))
# print('3: ', check_instance(True, int))
# print('4: ', check_instance('sdae', object))
# print('5: ', check_subclass(bool, object))
# print('6: ', check_subclass(bool, str))
# print('7: ', issubclass(int, int))
# print('8: ', check_subclass(bool, bool))
# print('9: ', check_subclass(bool, int))

