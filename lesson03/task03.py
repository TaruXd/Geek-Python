# Пункт 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def my_func(number1, number2, number3):
    try:
        my_list = [float(number1), float(number2), float(number3)]
        my_list.remove(min(my_list))
        return sum(my_list)
    except:
        return "Ошибка! Аргументы функции должы быть числовыми"

print("Вариант 1: ", my_func(100.4, 123, 30))


# Усложненный вариант
def my_func_mod(numbers, numbers_count=2):
    """
    Расчет суммы заданного количества максимальных значений из списка
    :param numbers: список из числовых значений
    :param numbers_count: количество элементов для суммирования
    """
    try:
        numbers.sort(reverse=-1)
        return float(sum(numbers[0:numbers_count]))
    except:
        return "Ошибка! Аргументы функции должы быть числовыми"

print("Вариант 2: ", my_func_mod([100.4, 123, 30, 40, 60, 100],numbers_count=2))


