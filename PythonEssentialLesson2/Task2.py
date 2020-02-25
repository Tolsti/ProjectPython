"""Опишите классы графического объекта, прямоугольника и объекта, который может обрабатывать нажатия мыши.
Опишите класс кнопки. Создайте объект кнопки и обычного прямоугольника. Вызовите метод нажатия на кнопку."""


class Rectangle:
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b


class ObjectSwitch:
    def click_button(self):
        if not Button.switch:
            Button.switch = True
        else:
            Button.switch = False


class Button(Rectangle):
    switch = False


if __name__ == '__main__':
    button = Button(4, 8)
    rectangle = Rectangle(3, 7)
    obj = ObjectSwitch()
