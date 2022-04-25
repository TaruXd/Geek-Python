# Задание 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор. Функция должна вызываться
# следующим образом: for el in fact(n). Функция отвечает за получение факториала числа,
# а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

# Не до конца ясно задание, поэтому сделаю, как понял.

# Функция, вовзращающая генератор
def generator(number):
    for element in range(1, number+1):
        yield element

# Функция, возвращающая факториал числа
def factorial(number):
    result = 1
    numbers = [el for el in generator(number)]
    for x in numbers:
        result *= x
        print(f"{x}! = {result}")
    return result

while True:
    n = input("Введите целое число: ")
    try:
        n = int(n)
        print(f"Факториал числа {n} равен {factorial(n)}")
        break
    except:
        print("Ошибка! Формат запрашиваемых данных не соответствует введенному!")
