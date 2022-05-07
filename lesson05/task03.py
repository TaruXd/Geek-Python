# Задание 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
# и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
#
# Иванов 23543.12
# Петров 13749.32

import codecs
from statistics import mean

try:
    target_salary = float(input("Введите целевой уровень ЗП: "))
    with codecs.open('task03.txt', 'r', 'utf-8') as my_file:
        salaries = []
        lower_workers = []
        for line in my_file.readlines():
            row = line.split(" ")
            salaries.append(float(row[1]))
            if float(row[1]) < target_salary:
                lower_workers.append(row[0])
    avg_salary = mean(salaries)
    if len(lower_workers) > 0:
        print(f"Перечень сотрудников с окладом менее {target_salary}: {lower_workers}")
    else:
        print("Все сотрудники получаю ЗП выше целевой")
    print("Средняя ЗП составляет: " + "{:.2f}".format(avg_salary))
except ValueError:
    print("Введены некорректные данные по целевой ЗП")

