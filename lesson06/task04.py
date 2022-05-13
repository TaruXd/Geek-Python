# Задание 4.Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую
# скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    name: str
    speed: float
    color: str
    is_police: bool = False

    def __init__(self, name, speed, color):
        self.name = name
        self.speed = speed
        self.color = color

    def go(self):
        print(f"Car {self.name} started moving")

    def stop(self):
        print(f"Car {self.name} stopped")

    def turn(self, direction):
        if direction in [-1, 1]:
            if direction == -1:
                print(f"Car {self.name} turned left")
            else:
                print(f"Car {self.name} turned right")
        else:
            raise ValueError("Direction attribute can be -1 (left) or 1 (right)")

    def show_speed(self):
        print(f"Speed: {self.speed}")


class TownCar(Car):

    def show_speed(self):
        max_speed = 60
        if self.speed > max_speed:
            print(f"Speed: {self.speed} > max ({max_speed}) allowed")
        else:
            print(f"Speed: {self.speed}")


class WorkCar(Car):

    def show_speed(self):
        max_speed = 40
        if self.speed > max_speed:
            print(f"Speed: {self.speed} > max ({max_speed}) allowed")
        else:
            print(f"Speed: {self.speed}")


class SportCar(Car):
    nitro_boost: float

    def __init__(self, name, speed, color, nitro_boost):
        super().__init__(name, speed, color)
        self.nitro_boost = nitro_boost

    def nitro_speed(self):
        print(f"Nitro speed: {self.speed + self.nitro_boost}")


class PoliceCar(Car):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color)
        self.is_police = True


print("\nПример вывода атрибутов и методов класса:")

town_car_1 = TownCar("Town_car_1", 59, "Red")
print(f"{town_car_1.name} colour is {town_car_1.color}")
print(f"Is {town_car_1.name} police: {town_car_1.is_police}")
town_car_1.go()
print(f"{town_car_1.name} speed is:")
town_car_1.show_speed()
town_car_1.turn(1)
town_car_1.turn(-1)
town_car_1.stop()


police_car = PoliceCar("Police_car", 90, "Black")
print(f"\n{police_car.name} colour is {police_car.color}")
print(f"Is {police_car.name} police: {police_car.is_police}")

print("\nПример вывода переопределения методов класса:")

town_car_2 = TownCar("Town_car_2", 61, "Blue")
print(f"{town_car_2.name} speed is:")
town_car_2.show_speed()

print("\nПример вывода переопределения методов класса:")

work_car = WorkCar("Work_car", 41, "Blue")
print(f"{work_car.name} speed is:")
work_car.show_speed()

print("\nПример вывода новых атрибутов и методов дочернего класса:")

sport_car = SportCar("Sport_car_1", 100, "Blue", 20)
print(f"{sport_car.name} speed is:")
sport_car.show_speed()
sport_car.nitro_speed()
