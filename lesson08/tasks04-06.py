# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом
# классе определить параметры, общие для приведенных типов. В классах-наследниках
# реализовать параметры, уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём
# оргтехники на склад и передачу в определенное подразделение компании. Для хранения
# данных о наименовании и количестве единиц оргтехники, а также других данных, можно
# использовать любую подходящую структуру, например словарь.
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
# пользователем данных. Например, для указания количества принтеров, отправленных
# на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники»
# максимум возможностей, изученных на уроках по ООП.
import sys
from abc import ABC, abstractmethod


def str_to_class(classname):
    return getattr(sys.modules[__name__], classname)


class NotFoundItems(Exception):
    def __init__(self, wrong_keys: list):
        self.wrong_keys = wrong_keys

    def __str__(self):
        return f"Товары {', '.join(self.wrong_keys)} не найдены. Операция отменена"


class NotEnoughItems(Exception):
    def __init__(self, wrong_values_keys: list):
        self.wrong_values_keys = wrong_values_keys

    def __str__(self):
        return f"Количество товаров {', '.join(self.wrong_values_keys)} для отправки превышает текущее наличие на складе. Операция отменена"


class MaxCapacityExceeded(Exception):

    def __init__(self, max_capacity):
        self.max_capacity = max_capacity

    def __str__(self):
        return f"Превышается максимальное количество товаров ({self.max_capacity}) на складе. Операция отменена"


class OEStorage:
    name: str
    max_capacity: int = 1
    current_storage: dict = {}

    @property
    def total_items_count(self):
        return sum(self.current_storage.values())

    def __init__(self, name: str, max_capacity: int):
        self.name = name
        self.max_capacity = max_capacity

    def receive_items(self, items_to_add: dict):
        print(f"Запуск операции получения товаров на склад склада\nПеречень товаров для получения: {items_to_add}")
        try:
            if sum(self.current_storage.values()) + sum(items_to_add.values()) < self.max_capacity:
                for key, value_to_add in items_to_add.items():
                    if key in self.current_storage.keys():
                        current_value = self.current_storage.get(key)
                        self.current_storage.update({key: current_value + value_to_add})
                    else:
                        self.current_storage.update({key: value_to_add})
            else:
                raise MaxCapacityExceeded(self.max_capacity)
        except MaxCapacityExceeded:
            print(MaxCapacityExceeded(self.max_capacity))

    def send_items(self, items_to_send: dict):
        print(f"Запуск операции отправки товаров со склада\nПеречень товаров для отправки: {items_to_send}")
        current_storage_backup = self.current_storage.copy()
        wrong_keys = []
        wrong_values_keys = []
        for key, value in items_to_send.items():
            if self.current_storage.get(key) != None:
                current_value = self.current_storage.get(key)
                if value < current_value:
                    self.current_storage.update({key: current_value - value})
                else:
                    wrong_values_keys.append(key)
            else:
                wrong_keys.append(key)
        try:
            if wrong_values_keys != []:
                self.current_storage = current_storage_backup.copy()
                raise NotEnoughItems(wrong_values_keys)
        except NotEnoughItems:
            print(NotEnoughItems(wrong_values_keys))
        try:
            if wrong_keys != []:
                self.current_storage = current_storage_backup.copy()
                raise NotFoundItems(wrong_keys)
        except NotFoundItems:
            print(NotFoundItems(wrong_keys))

    def get_items_info(self, equip_type: str, model: str):
        pass



class OfficeEquipment(ABC):
    model: str
    price: float
    equip_type: str

    def __init__(self, model: str, price: float):
        self.model = model
        self.equip_type = str(self.__class__.__name__)
        self.price = price

    @property
    @abstractmethod
    def guarantee_period(self):
        pass


class Printer(OfficeEquipment):
    is_colored: bool

    def __init__(self, model: str, price: float, is_colored: bool):
        super().__init__(model, price)
        self.is_colored = is_colored

    @property
    def guarantee_period(self):
        if self.is_colored:
            return self.price // 100
        else:
            return self.price // 50


class Scanner(OfficeEquipment):
    dpi: int

    def __init__(self, model: str, price: float, dpi: int):
        super().__init__(model, price)
        self.dpi = dpi

    @property
    def guarantee_period(self):
        if self.dpi > 350:
            return self.price // 90
        else:
            return self.price // 50


class Xerox(OfficeEquipment):
    dpi: int
    is_colored: bool

    def __init__(self, model: str, price: float, is_colored: bool, dpi: int):
        super().__init__(model, price)
        self.is_colored = is_colored
        self.dpi = dpi

    @property
    def guarantee_period(self):
        if self.is_colored or self.dpi > 350:
            return self.price // 120
        else:
            return self.price // 45

def get_eqipment_info(args: list[object]):
    result = []
    for el in range(len(args)):
        result.append([hash(args[el]), args[el].__dict__])
    return result

storage_1 = OEStorage("Moscow", 10)

printer_1 = Printer("printer_1", 1000, True)
printer_2 = Printer("printer_2", 2000, True)

scanner_1 = Scanner("scanner_1", 500, 420)
scanner_2 = Scanner("scanner_2", 750, 480)

xerox_1 = Xerox("xerox_1", 250, True, 300)
xerox_2 = Xerox("xerox_2", 350, True, 350)

equipment = [printer_1, printer_2, scanner_1, scanner_2, xerox_1, xerox_2]


eqipment_info = get_eqipment_info([printer_1, scanner_2, scanner_1, scanner_1])
print("Перечень текущих доступных объектов: ")
print(*eqipment_info, sep="\n")

request_equipmnet = input("Введите название модели: ")


def str_to_equimplent_dict(request_equipmnet: str):
    success = False
    for x in equipment:
        if request_equipmnet == x.__dict__.get('model'):
            success = True
            return x.__dict__
    if not success:
        return None


print(str_to_equimplent_dict(request_equipmnet))




# storage_1.receive_items({"xerox": 4, "printer": 2, "scanner": 3})
# print(f"Остатки на складе: {storage_1.current_storage}\nИтого товаров: {storage_1.total_items_count}\n")
# storage_1.send_items({"xerox": 1, "printer": 1, "scanner": 2})
# print(f"Остатки на складе: {storage_1.current_storage}\nИтого товаров: {storage_1.total_items_count}\n")
# storage_1.send_items({"xeroxsdf": 1, "printer": 2, "scanner": 1})
# print(f"Остатки на складе: {storage_1.current_storage}\nИтого товаров: {storage_1.total_items_count}\n")

