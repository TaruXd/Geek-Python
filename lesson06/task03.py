# Задание 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход). Последний атрибут должен
# быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность)
# на базе класса Worker. В классе Position реализовать методы получения полного
# имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    name: str
    surname: str
    position: str
    _income: dict

    def __init__(self, name: str, surname: str, position: str, wage: float, bonus: float):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return sum(self._income.values())


worker_1 = Position("John", "Doe", "Engineer", 1000, 250)
worker_2 = Position("Lady", "Gaga", "Singer", 100000, 3000)

print(f"Личность: {worker_1.get_full_name()}")
print(f"Должность: {worker_1.position}")
print(f"Доход: {worker_1.get_total_income()}\n")

print(f"Личность: {worker_2.get_full_name()}")
print(f"Должность: {worker_2.position}")
print(f"Доход: {worker_2.get_total_income()}")
