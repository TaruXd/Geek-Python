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
import json
import os.path

from abc import ABC, abstractmethod


def str_to_class(classname):
    return getattr(sys.modules[__name__], classname)


class NotFoundItems(Exception):
    def __init__(self, wrong_keys: list):
        self.wrong_keys = wrong_keys

    def __str__(self):
        return f"\033[31mТовары {', '.join(self.wrong_keys)} не найдены на складе. Операция отменена\033[0m"


class NotEnoughItems(Exception):
    def __init__(self, wrong_values_keys: list):
        self.wrong_values_keys = wrong_values_keys

    def __str__(self):
        return f"\033[31mКоличество товаров {', '.join(self.wrong_values_keys)} для отправки превышает текущее наличие на складе. Операция отменена\033[0m"


class MaxCapacityExceeded(Exception):

    def __init__(self, max_capacity):
        self.max_capacity = max_capacity

    def __str__(self):
        return f"\033[31mПревышается максимальное количество товаров ({self.max_capacity}) на складе. Операция отменена\033[0m"


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


printer_1 = Printer("printer_1", 1000, True)
printer_2 = Printer("printer_2", 2000, True)

scanner_1 = Scanner("scanner_1", 500, 420)
scanner_2 = Scanner("scanner_2", 750, 480)

xerox_1 = Xerox("xerox_1", 250, True, 300)
xerox_2 = Xerox("xerox_2", 350, True, 350)

equipment = [printer_1, printer_2, scanner_1, scanner_2, xerox_1, xerox_2]

eqipment_info = get_eqipment_info(equipment)


def str_to_equimpent_dict(request_equipment: str):
    success = False
    for x in equipment:
        if request_equipment == x.__dict__.get('model'):
            success = True
            return x.__dict__
    if not success:
        return None


def str_to_equipment_hash(request_equipment: str):
    success = False
    for x in equipment:
        if request_equipment == x.__dict__.get('model'):
            success = True
            return hash(x)
    if not success:
        return None


class OEStorage:
    name: str
    max_capacity: int = 1
    current_storage: list[dict] = []

    @staticmethod
    def total_items_count(items: list[dict]):
        result = 0
        if items == []:
            return result
        for el in items:
            result += el.get('amount')
        return result

    def __init__(self, name: str, max_capacity: int):
        self.name = name
        self.max_capacity = max_capacity
        if os.path.exists("./storage_1.json"):
            with open("storage_1.json") as data:
                self.current_storage = json.load(data)


    def receive_items(self, items_to_add: list[dict]):
        print(f"\033[33m\nЗапуск операции получения товаров на склад склада\n\033[0mПеречень товаров для получения:")
        print(*items_to_add, sep="\n")
        try:
            if self.total_items_count(self.current_storage) + self.total_items_count(items_to_add) < self.max_capacity:
                for el_to_add in items_to_add:
                    for el_storage in self.current_storage:
                        if el_storage.get('hash') == el_to_add.get('hash'):
                            current_amount = el_storage.get('amount')
                            el_storage.update({"amount": el_storage.get('amount') + el_to_add.get('amount')})
                            # items_to_add.remove(el_to_add)
                    self.current_storage.append(el_to_add)
                print("\033[32mТовары успешно добавлены\033[0m")
                with open('storage_1.json', 'w') as file_json:
                    json.dump(self.current_storage, file_json)
            else:
                raise MaxCapacityExceeded(self.max_capacity)
        except MaxCapacityExceeded:
            print(MaxCapacityExceeded(self.max_capacity))

    def send_items(self, items_to_send: list[dict]):
        print(f"\033[33m\nЗапуск операции отправки товаров со склада\nПеречень товаров для отправки:\033[0m")
        print(*items_to_send, sep="\n")
        current_storage_backup = self.current_storage.copy()
        wrong_keys = []
        wrong_values_keys = []
        for el_to_send in items_to_send:
            for el_storage in self.current_storage:
                if el_to_send.get('hash') == el_storage.get('hash'):
                    value_to_send = el_to_send.get('amount')
                    current_value = el_storage.get('amount')
                    if value_to_send <= current_value:
                        el_storage.update({"amount": current_value - value_to_send})
                        items_to_send.remove(el_to_send)
                    else:
                        wrong_values_keys.append(el_to_send.get('model'))
        wrong_keys.extend(el_to_send.get('model') for el_to_send in items_to_send)
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

        if self.current_storage != current_storage_backup:
            print("\033[32mТовары успешно отправлены\033[0m")
            with open('storage_1.json', 'w') as file_json:
                json.dump(self.current_storage, file_json)

    def __str__(self):
        if len(self.current_storage) == 0:
            return "\nСклад пуст"
        show = "\nТекущие остатки на складе: \n"
        for el in self.current_storage:
            show += str({'hash': el.get('hash')}) + " " + \
                    str({'model': el.get('model')}) + " " +\
                    str({'amount': el.get('amount')}) + " " + "\n"
        return show

    def get_items_info(self, hash):
        for el_storage in self.current_storage:
            if el_storage.get('hash') == hash:
                return el_storage
        return f"Заданный товар не найден"


def process_requests_equipment(input_data: str):
    result = {}
    requests_equipment = input_data.split()

    if len(requests_equipment) != 2:
        return f"\033[31mВводимые данные должны содержать название модели и её количество, разделенные пробелом\033[0m"
    model, amount = requests_equipment[0], requests_equipment[1]

    if str_to_equipment_hash(model) != None:
        result.update({"hash": str_to_equipment_hash(model)})
        result.update(str_to_equimpent_dict(model))
    else:
        return f"\033[31mТовара {model} не существует\033[0m"
    try:
        amount = int(amount)

        if amount > 0:
            result.update({"amount": amount})
        else:
            return f"\033[31mКоличество товара не может отрицательным\033[0m"
        return result
    except:
        return "\033[31mКоличество товара должно быть натуральным числом\033[0m"



def form_request_equipment_list():
    print("\033[33m\nФормирование списка товаров\033[0m")
    equipment_list = []
    while True:
        input_data = input("Введите название модели и количество через пробел\nили Enter для завершения формирования списка: ")
        if input_data != "":
            attempt = process_requests_equipment(input_data)
            if isinstance(attempt, dict):
                equipment_list.append(attempt)
            else:
                print(attempt)
        else:
            break

    return equipment_list



storage_1 = OEStorage("Moscow", 10)


def update_storage_items_hash(items_to_refresh: list[dict], equipment):
    for el in items_to_refresh:
        for x in equipment:
                if el.get('model') == x.__dict__.get('model'):
                    el.update({'hash': hash(x)})


update_storage_items_hash(storage_1.current_storage, equipment)

while True:
    try:
        print("\nПеречень доступных команд:\n"
              "1 - Просмотр доступных товаров\n"
              "2 - Просмотр текущих остатков на складе\n"
              "3 - Добавление товаров на склад\n"
              "4 - Отправка товаров со склада\n"
              "5 - Просмотр информации о товаре на складе\n"
              "6 - Изменить максимальную вместимость склада\n"
              "7 - Выход из программы")
        action = int(input("Введите номер команды для выполнения: "))
        if action < 1 or action > 7:
            raise Exception
        match action:
            case 1:
                print("\nПеречень текущих доступных товаров: ")
                print(*eqipment_info, sep="\n")
            case 2:
                print(storage_1)
            case 3:
                request_equipment_list = form_request_equipment_list()
                storage_1.receive_items(request_equipment_list)
            case 4:
                request_equipment_list = form_request_equipment_list()
                storage_1.send_items(request_equipment_list)
            case 5:
                item = input("Введите название товара: ")
                print(storage_1.get_items_info(str_to_equipment_hash(item)))
            case 6:
                print(f"\nТекущая максимальная вместимость склада равна: {storage_1.max_capacity}")
                current_total_items = storage_1.total_items_count(storage_1.current_storage)
                try:
                    new_max_capacity = int(input("Введите требуемую максимальную вместимость склада: "))
                    if new_max_capacity >= 0 and new_max_capacity >= current_total_items:
                        storage_1.max_capacity = new_max_capacity
                        print("\033[32mМаксимальная вместимость склада успешно изменена\033[0m")
                    else:
                        raise Exception
                except Exception:
                    print(f"\033[31mЗначение максимальной вместимости склада должно быть натуральным числом и не меньше текущего количества товаров {current_total_items} на складе\033[0m")
            case 7:
                exit()
    except Exception:
        print("\033[31mНе найдена выбранная команда, введите повторно\033[0m")
