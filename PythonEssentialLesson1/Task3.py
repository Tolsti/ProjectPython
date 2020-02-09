"""Используя ссылки в конце данного урока, ознакомьтесь с таким средством инкапсуляции как свойства.
Ознакомьтесь с декоратором property в Python. Создайте класс, описывающий температуру и позволяющий
задавать и получать температуру по шкале Цельсия и Фаренгейта, причём данные могут быть заданы в
одной шкале, а получены в другой."""


class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature

    def to_fahrenheit(self):
        return (self._temperature * 1.8) + 32

    @property
    def temperature(self):
        # print('Полученное значение: ')
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        # print('Задать значение: ')
        self._temperature = value


man = Celsius()
man.temperature = 37
print(man.temperature)
print(man.to_fahrenheit())
