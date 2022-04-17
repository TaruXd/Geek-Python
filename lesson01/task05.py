# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек,
# или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

earnings = input("Введите значение выручки (руб.):")
costs = input("Введите значение издержек (руб.):")
check_number_error = "Ошибка! Значения должны быть целыми положительными числами"
check_employee_count_error = "Ошибка! Количество сотрудников должно быть целым положительным числом"
while True:
    error = 0
    try:
        earnings = float(earnings)  # проверка на тип значения "Число"
        costs = float(costs)  # проверка на тип значения "Число"
        if earnings <= 0 or costs <= 0:  # проверка на положительность значений
            error = 1
            print(check_number_error)
        else:
            result = earnings - costs
            if result > 0:
                print("Прибиль компании составила {} руб.".format(result))
                profitability = result/earnings
                print("Рентабельность выручки компании равна {}".format(profitability))
                employee_count = input("Введите количество сотрудников: ")
                while True:
                    try:
                        employee_count = int(employee_count)  # проверка на целочисленность значения
                        if employee_count > 0:  # проверка на положительность значения
                            employee_profit_ratio = result/employee_count
                            print("Прибыль фирмы в расчете на одного сотрудника равна {} руб.".format(employee_profit_ratio))
                        else:
                            print(check_employee_count_error)
                    except ValueError:
                        error = 1
                        print(check_employee_count_error)
                    if error == 0:
                        break
                    employee_count = input("Введите количество сотрудников повторно: ")
            else:
                print("Убытки компании составили {} руб.".format(result))
    except ValueError:
        error = 1
        print(check_number_error)
    if error == 0:
        break
    earnings = input("Введите значение выручки (руб.) повторно:")
    costs = input("Введите значение издержек (руб.) повторно:")
# цикл реализован для повторного запроса данных в случае ввода некорректных