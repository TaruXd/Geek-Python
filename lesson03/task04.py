# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

# Вариант 1 через **
def my_func_1(number: float, power: int):
    error = 0
    error_message = "Ошибка! "
    if number <= 0:
        error_message = error_message + "Число должно быть действительным положительным числом.\n"
        error = 1
    if power >= 0:
        error_message = error_message + "Степень должна быть целым отрицательным числом."
        error = 1
    if error != 1:
        result = number ** power
        return float(result)
    else:
        return error_message

# Вариант 2 через цикл
def my_func_2(number: float, power: int):
    error = 0
    error_message = "Ошибка! "
    if number <= 0:
        error_message = error_message + "Число должно быть действительным положительным числом.\n"
        error = 1
    if power >= 0:
        error_message = error_message + "Степень должна быть целым отрицательным числом."
        error = 1
    if error != 1:
        result = 1
        for step in range(abs(power)):
            result = result / number
        return float(result)
    else:
        return error_message
while True:
    try:
        x = float(input("Введите число (действительное положительное), которое нужно вовзести  в степень: "))
        y = int(input("Введите степень (целое отрицатльное), в которую нужно возвести число: "))
        result_1 = my_func_1(x, y)
        result_2 = my_func_2(x, y)
        if isinstance(result_1, float) or isinstance(result_2, float):
            print(f"Результат по 1-му варианту: {result_1:.5f}")
            print(f"Результат по 2-му варианту: {result_2:.5f}")
            break
        else:
            print(result_1)
            print(result_2)
            continue
    except:
        continue
