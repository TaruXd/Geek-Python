# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
# список только числами. Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не
# остановит работу скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный
# список с числами выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. При вводе
# пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список,
# только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число) и
# отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.

class MyCheckFloatException(Exception):

    def __init__(self, element: str):
        self.element = element

    def __str__(self):
        return f"Элемент списка '{self.element}' не является числом и будет проигнорирован"

my_list = []
while True:


    new_input = input("Введите числа, разделенные пробелом, для добавления в спискок или stop для выхода: ")

    if new_input == "stop":
        print(f"Заданный спискок:\n {my_list}")
        break

    new_elements = new_input.split()

    for el in new_elements:
        try:
            if el.isdigit():
                my_list.append(el)
            else:
                raise MyCheckFloatException(el)
        except MyCheckFloatException:
            print(MyCheckFloatException(el))


