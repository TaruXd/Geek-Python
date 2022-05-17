# Задание 2. Реализовать класс Road (дорога), в котором определить
# атрибуты: length (длина), width (ширина). Значения данных атрибутов
# должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
# необходимого для покрытия всего дорожного полотна. Использовать формулу:
# длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна. Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т

class Road:
    _length: float
    _width: float
    _weight: float

    def __init__(self, lenght: float, width: float, weight: float):
        self._length = lenght
        self._width = width
        self._weight = weight

    def square(self, thickness):
        return self._length * self._width * thickness * self._weight / 1000


road_1 = Road(10, 20, 25)

print(f"Square calculcation result: {road_1.square(5)}")
