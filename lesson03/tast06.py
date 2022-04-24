# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов,
# разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().
import re


def int_func(words):
    result = ""
    if words == words.lower() and re.search(r'[^a-z ]', words) == None:
        words = words.split(" ")
        for pos in range(len(words)):
            result += words[pos].lower().capitalize() + " "
        return result.rstrip(" ")
    else:
        return "Ошибка! Строка должна быть из слов на латинице и в нижнем регистре"

words = input("Введите строку из слов, разделенных пробелом: ")

print(int_func(words))