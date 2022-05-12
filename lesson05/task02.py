# Задание 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.


import codecs
with codecs.open('task02.txt', 'r', 'utf-8') as my_file:
    counter = 0
    row = my_file.readline()
    while row != "":
        counter += 1
        words_in_row = len(row.split(" "))
        row = my_file.readline()
        print(f"Количество слов в строке {counter} равно {words_in_row}")

print(f"Итого количество строк в файле равно {counter}")
