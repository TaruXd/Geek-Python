# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

number = input("Введите число n:")
check_number_error = "Значение должно быть целым положительным числом"
while True:
    error = 0
    try:
        number = int(number)  # проверка на целочисленность значения
        if number > 0:  # проверка на положительность значения
            calculation_level1 = int(number)
            calculation_level2 = int(str(number) + str(number))
            calculation_level3 = int(str(number) + str(number) + str(number))
            result = calculation_level1 + calculation_level2 + calculation_level3
            print("Результат расчета по формуле n + nn + nnn равен ", result)
        else:
            error = 1
            print(check_number_error)
    except ValueError:
        error = 1
        print(check_number_error)
    if error == 0:
        break
    number = input("Введите число повторно:")
# цикл реализован для повторного запроса данных в случае ввода некорректных