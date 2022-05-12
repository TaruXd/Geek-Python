# Задание 7. Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
# а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки,
# также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
#
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

from statistics import mean
import json

firms_dict = {}
avg_profit_dict = {"average_profit": None}

with open('task07.txt', 'r') as my_file:
    for line in my_file.readlines():
        line = line.split(" ")
        profit = float(line[2]) - float(line[3])
        firms_dict.update({line[0]: profit})

avg_profit_dict.update(average_profit=mean(prof for prof in firms_dict.values() if prof >= 0))

result = [firms_dict, avg_profit_dict]
print(result)

with open('task07.json', 'w') as file_json:
    json.dump(result, file_json)
