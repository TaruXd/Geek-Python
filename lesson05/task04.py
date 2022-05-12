# Задание 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
#
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

import codecs
import os

try:
    eng_file_name = input("Введите полное имя файла (с его типом), где сдержатся исходные строки: ")

    if os.path.exists('task04_ru.txt'):
        os.remove('task04_ru.txt')

    en_ru = {"one": "один", "two": "два", "three": "три", "four": "четыре"}

    with codecs.open(eng_file_name, 'r', 'utf-8') as my_file:
        for line in my_file.readlines():
            words = line.lower().split(" ")
            with codecs.open('task04_ru.txt', 'a', 'utf-8') as new_file:
                new_file.write(line.lower().replace(words[0], en_ru.get(words[0])).capitalize())

    print("Проверьте результат перевода в файле task04_ru.txt в директории исполняемого py-файла")
except:
    print("Указанный файл в директории исполняемого py-файла не найден")