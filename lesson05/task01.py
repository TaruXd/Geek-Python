# Задание 1. Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

# Кодек требуется для обеспечения возможности ввода символов кириллицы
import codecs

with codecs.open('task01.txt', 'w', 'utf-8') as my_file:
    my_file.write("")

with codecs.open('task01.txt', 'a', 'utf-8') as my_file:
    input_str = "0"
    while input_str != "":
        input_str = input("Введите строку или завршите ввод пустой строкой: ")
        my_file.write(input_str + "\n")

with codecs.open('task01.txt', 'r', 'utf-8') as my_file:
    print("Результат ввода: \n" + my_file.read())

print("Проверьте файл task01.txt в директории исполняемого py-файла")
