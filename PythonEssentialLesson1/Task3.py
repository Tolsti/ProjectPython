"""Используя ссылки в конце данного урока, ознакомьтесь с таким средством инкапсуляции как свойства.
Ознакомьтесь с декоратором property в Python. Создайте класс, описывающий температуру и позволяющий
задавать и получать температуру по шкале Цельсия и Фаренгейта, причём данные могут быть заданы в
одной шкале, а получены в другой."""


class Temperature:
    def __init__(self, temperature = 0):
        self.set_temperature(temperature)
    
    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32
    
    def get_temperature(self):
        return self._temperature
    
    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value


man = Temperature()
man.set_temperature(-300)
print(man.get_temperature())
print(man.to_fahrenheit())
