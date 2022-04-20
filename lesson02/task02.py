# Пункт 2. Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

my_list = list(input("Введите последовательность сивмолов списка: "))
max_index = len(my_list)
stop_index = max_index if max_index % 2 == 0 else max_index - 2
for pos in range(0, stop_index, 2):
    my_list[pos], my_list[pos + 1] = my_list[pos + 1], my_list[pos]
print(my_list)
