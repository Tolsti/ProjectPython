"""Создайте класс, описывающий автомобиль. Создайте класс автосалона, содержащий в себе список автомобилей,
доступных для продажи, и функцию продажи заданного автомобиля."""


class Car:
    make = None
    model = None
    color = None
    price = None
    
    def __init__(self, make, model, color, price):
        self.make = make
        self.model = model
        self.color = color
        self.price = price


class MotorShow:
    list_cars = list()
    
    def buy_car(self):
        # print('Выберите автомобиль который хотите купить:')
        for i in range(len(self.list_cars)):
            print(i + 1, self.list_cars[i].make, self.list_cars[i].model, self.list_cars[i].color,
                  self.list_cars[i].price)
        result = int(input('Выберите автомобиль который хотите купить: '))
        if result <= len(self.list_cars):
            print('Вы купили:')
            print(self.list_cars[result - 1].make, self.list_cars[result - 1].model, self.list_cars[result - 1].color,
                  self.list_cars[result - 1].price)
            self.list_cars.pop(result - 1)
        else:
            print('Нет такого автомобиля.')


motor_show = MotorShow()

motor_show.list_cars.append(Car('Skoda', 'Superb', 'black', 9000))
motor_show.list_cars.append(Car('BMW', 'X3', 'black', 6700))
motor_show.list_cars.append(Car('Honda', 'Civic', 'blue', 4500))
motor_show.list_cars.append(Car('Toyota', 'Avalon', 'white', 11000))
motor_show.list_cars.append(Car('Nissan', 'Altima', 'red', 4000))

motor_show.buy_car()
motor_show.buy_car()
