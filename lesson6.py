

#2--------------------------------------------------

class Road:

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass(self):
        mass = self._length * self._width * 25 * 5 / 1000
        return(mass)

road_1 = Road(20, 20)
print(road_1.mass())

#3---------------------------------------------------

class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"Оклад": 1000, "Премия": 200}

class Position(Worker):
    def __init__(self, name, surname, position):
        super().__init__(name, surname, position)

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self._income.get("Оклад") + self._income.get("Премия")

worker_1 = Position("John", "Smith", "CEO")
print(worker_1.get_full_name())
print(worker_1.position)
print(worker_1.get_total_income())

#4--------------------------------------------------------

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        print(f"Машина повернула {direction}")

    def show_speed(self, speed):
        print(f"Текущая скорость автомобиля {speed}")

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self, speed):
        if speed > 60:
            print("Превышение скорости!")
        else:
            print(f"Текущая скорость автомобиля {speed}")

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self, speed):
        if speed > 40:
            print("Превышение скорости!")
        else:
            print(f"Текущая скорость автомобиля {speed}")

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

car_1 = TownCar(70, "red", "Alfa", None)
car_2 = SportCar(150, "yellow", "Ferrari", None)
car_3 = WorkCar(50, "black", "Cleaner", None)
car_4 = PoliceCar(75, "white", "Police", True)

print(car_1.show_speed(70))
print(car_1.go())
print(car_1.stop())
print(car_1.turn("налево"))

print(car_1.show_speed(60))
print(car_3.show_speed(40))

print(car_4.is_police)
print(car_3.name)
print(car_2.color)
print(car_1.speed)

#5-----------------------------------------------

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Ручка не стирается! Помните об этом.")

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Карандаш пишет даже в космосе...")

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("На самом деле это не маркер, а подводка для бровей.")

item_1 = Pen("Ручка")
print(item_1.draw())

item_2 = Pencil("Карандаш")
print(item_2.draw())

item_3 = Handle("Маркер")
print(item_3.draw())

item_4 = Stationery("Маркер")
print(item_4.draw())
