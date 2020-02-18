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

class Horse:
    def run(self):
        print('I am running')


class Bird:
    def fly(self):
        print('I am flying')


class Pegasus(Horse, Bird):
    pass


def main():
    pegasus = Pegasus()
    pegasus.run()
    pegasus.fly()


if __name__ == '__main__':
    main()
