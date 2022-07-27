# Задание 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату
# в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date:
    _date: str

    def __init__(self, date: str):
        self._date = date

    @staticmethod
    def date_check(date_parts_dict: dict):
        error_message = ""
        if date_parts_dict.get("День") <= 0 or date_parts_dict.get("День") > 31:
            error_message += "Число должно быть от 1 до 31\n"
        if date_parts_dict.get("Месяц") <= 0 or date_parts_dict.get("Месяц") > 12:
            error_message += "Месяц должен быть от 1 до 12\n"
        if date_parts_dict.get("Год") < 0:
            error_message += "Год должен быть больше нуля"
        if error_message == "":
            return True
        else:
            return error_message

    @classmethod
    def date_parts(cls, _date: str):
        parts_list = _date.split("-")
        try:
            date_parts_dict = {"День": int(parts_list[0]),
                               "Месяц": int(parts_list[1]),
                               "Год": int(parts_list[2])}

            if cls.date_check(date_parts_dict) == True:
                print(date_parts_dict)
            else:
                print(cls.date_check(date_parts_dict))

        except:
            print("Вводимая дата должна быть в формате 'число-месяц-год'")


while True:
    date = input("Введите дату в формате 'число-месяц-год' или Enter для выхода:")
    if date == "":
        exit()
    else:
        Date.date_parts(date)


