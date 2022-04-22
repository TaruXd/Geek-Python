# Пункт 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def devide(var_1, var_2):
    try:
        return var_1 / var_2
    except ZeroDivisionError:
        return "Ошибка! Деление на ноль."

while True:
    error = 0
    try:
        number_1, number_2 = float(input("Введите первое число: ")), float(input("Введите второе число: "))
        print(devide(number_1, number_2))
    except BaseException:
        error = 1
        print("Ошибка! Введены данные некорректных типов")
    if error == 0:
        break