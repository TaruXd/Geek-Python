# Задание 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
from sys import argv


def salary_func(hours, rate, bonus):
    return print(hours * rate + bonus)

scrtipt_name, hours, rate, bonus = argv


print(scrtipt_name)
try:
    salary_func(int(hours), float(rate), float(bonus))
except:
    print("Invalid parameters")