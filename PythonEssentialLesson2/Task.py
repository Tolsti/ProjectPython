"""Создайте иерархию классов транспортных средств. В общем классе опишите общие для всех транспортных средств поля,
в наследниках – специфичные для них. Создайте несколько экземпляров.
Выведите информацию о каждом транспортном средстве."""


class Vehicle:
    def __init__(self):
        self.name = False
        self.can_ride = False
        self.can_swim = False
        self.can_fly = False
    
    def show_functions(self):
        print(str(self.name) + ':')
        print('Ездит: ', self.can_ride)
        print('Плавает: ', self.can_swim)
        print('Летает: ', self.can_fly)
        print()


class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.name = 'Машина'
        self.can_ride = True


class Boat(Vehicle):
    def __init__(self):
        super().__init__()
        self.name = 'Лодка'
        self.can_swim = True


class Plane(Vehicle):
    def __init__(self):
        super().__init__()
        self.name = 'Самолет'
        self.can_fly = True


class Amphibious(Car, Boat):
    def __init__(self):
        super().__init__()
        self.name = 'Амфибия'


class Agent_007s_car(Car, Boat, Plane):
    def __init__(self):
        super().__init__()
        self.name = 'Машина агента 007'


if __name__ == '__main__':
    car = Car()
    boat = Boat()
    plane = Plane()
    amphibious = Amphibious()
    agent_007s_car = Agent_007s_car()
    
    car.show_functions()
    boat.show_functions()
    plane.show_functions()
    amphibious.show_functions()
    agent_007s_car.show_functions()
