# Задание 2. Создайте собственный класс-исключение,
# обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа
# должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class MyZeroDivisonException(Exception):

    def __str__(self):
        return "Знаменатель не может быть нулем"


while True:
    a = input("Введите делитель: ")
    b = input("Введите знаменатель: ")

    try:
        a = float(a)
        b = float(b)

        if b == 0:
            raise MyZeroDivisonException

        print(f"Результат: {a / b}")
        exit()
    except MyZeroDivisonException:
        print(MyZeroDivisonException())
    except ValueError:
        print("Вводимые значения должны быть числовыми")


