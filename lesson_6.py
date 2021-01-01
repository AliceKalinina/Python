# task_1
import time


class TrafficLight:
    _color = None
    _colors = ['red', 'yellow', 'green']

    def __init__(self):
        self._color = self._colors[0]

    def running(self):
        i = 0
        while i < 5:
            for el in TrafficLight._colors:
                print(el)
                i += 1
                time.sleep(1)


traffic = TrafficLight()
traffic.running()


# task_2
class Road:
    __length = None
    __width = None
    weigth = None
    tickness = None

    def __init__(self, length, width):
        self.length = length
        self.width = width
        print('Creat road_to_village object')

    def intake(self):
        self.weigth = 25
        self.tickness = 0.05
        intake = self.length * self.width * self.weigth * self.tickness / 1000
        print(f'Need {intake} tons for the building')


road_to_village = Road(20000, 6)
road_to_village.intake()


# task_3
class Worker:
    name = None
    surname = None
    position = None
    profit = None
    bonus = None

    def __init__(self, name, surname, position, profit, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.profit = profit
        self.bonus = bonus


class Position(Worker):
    def __init__(self, name, surname, position, profit, bonus):
        super().__init__(name, surname, position, profit, bonus)

    def get_full_name(self):
        return self.name + self.surname

    def get_full_profit(self):
        self.__income = {'profit': self.profit, 'bonus': self.bonus}
        return self.__income


manager = Position('Petr', 'Petrov', 'manager', 500, 100)
print(manager.get_full_name(), manager.get_full_profit())


# task_4
class Cars:
    name = None
    speed = None
    color = None
    is_police = False

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return "The car went"

    def stop(self):
        return "The car has stopped"

    def turn(self, direction):
        return "The car turned to " + direction


class TownCar(Cars):
    family = None

    def __init__(self, name, speed, color, family=True):
        super().__init__(name, speed, color)
        self.family = family


class SportCar(Cars):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color)


class WorkCar(Cars):
    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)


class PoliceCar(Cars):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color, True)


ford = TownCar('Ford', 60, 'black')
print(ford.name, ford.color, ford.speed, ford.is_police)
print(ford.go(), ford.turn('City'), ford.stop())
sport = SportCar('Ford', 180, 'red')
work1 = WorkCar('Ford', 90, 'white', True)
work2 = WorkCar('Audi', 90, 'white', False)
police = PoliceCar('Ford', 180, 'red')


# task_5
class Stationery:
    atr_title = 'Title'

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        print('Отрисовка ручкой')


class Pencil(Stationery):
    def draw(self):
        print('Отрисовка карандашом')


class Handle(Stationery):
    def draw(self):
        print('Отрисовка маркером')


my_pen = Pen()
my_pencil = Pencil()
my_handle = Handle()
my_pen.draw()
my_pencil.draw()
my_handle.draw()
