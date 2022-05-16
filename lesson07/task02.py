# Задание 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь
# определенное название. К типам одежды в этом проекте относятся пальто и
# костюм. У этих типов одежды существуют параметры: размер (для пальто) и
# рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные
# на этом уроке знания: реализовать абстрактные классы для основных классов
# проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def materials(self):
        pass


class Coat(Clothes):

    def __init__(self, name: str, size: float):
        super().__init__(name)
        self.size = size

    @property
    def materials(self):
        return round(self.size/6.5 + 0.5, 2)


class Suit(Clothes):

    def __init__(self, name: str, height: float):
        super().__init__(name)
        self.height = height

    @property
    def materials(self):
        return round(2 * self.height + 0.3, 2)


coat_1 = Coat("coat_1", 5)
print(f"Пальто: {coat_1.name}")
print(f"Расход ткани: {coat_1.materials}")

suit_1 = Suit("suit_1", 5)
print(f"Костюм: {suit_1.name}")
print(f"Расход ткани: {suit_1.materials}")

print(f"Общий расход такни: {sum([suit_1.materials, coat_1.materials])}")
