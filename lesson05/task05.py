# Задание 5. Создать (программно) текстовый файл,
# записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

numbers = "10 20 30 40 50"

with open('task05.txt', 'w') as my_file:
    my_file.write(numbers)

with open('task05.txt', 'r') as my_file:
    data = my_file.read().split(" ")

for idx in range(len(data)):
    data[idx] = float(data[idx])
print("Сумма чисел равна: " + str(sum(data)))