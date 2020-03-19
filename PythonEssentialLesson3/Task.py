"""Опишите свой класс исключения. Напишите функцию, которая будет выбрасывать данное исключение,
если пользователь введёт определённое значение, и перехватите это исключение при вызове функции."""


class MyException(Exception):
    def fun_exception(self):
        while True:
            value = int(input('Enter a value from 0 to 100: '))
            if 0 <= value <= 100:
                pass
            else:
                raise MyException('out of the range from 0 to 100')


my_exception = MyException()

try:
    my_exception.fun_exception()
except MyException as error:
    print('Intercepted MyException')
    print(error)