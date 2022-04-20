# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = input("Введите число:")
check_number_error = "Ошибка! Значение должно быть целым положительным числом"
while True:
    error = 0
    try:
        number = int(number)  # проверка на целочисленность значения
        if number <= 0:  # проверка на положительность значения
            error = 1
            print(check_number_error)
        else:
            curr_number = number
            max_digit = curr_number % 10
            while True:
                curr_number = curr_number // 10
                curr_digit = curr_number % 10
                if curr_digit > max_digit:
                    max_digit = curr_digit
                if curr_number == 0:
                    break
            print("Максимальное значение из цифр в заданном числе равно ", max_digit)
    except ValueError:
        error = 1
        print(check_number_error)
    if error == 0:
        break
    number = input("Введите число повторно:")
# цикл реализован для повторного запроса данных в случае ввода некорректных