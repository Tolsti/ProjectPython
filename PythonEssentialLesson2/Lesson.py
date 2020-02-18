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

class MethodContainer:
    def __init__(self, data):
        self.data = data

    def method(self):
        print('method invoked')
        print('data = ', self.data)


instance = MethodContainer(8)
print(type(MethodContainer.method))
print(type(instance.method))
