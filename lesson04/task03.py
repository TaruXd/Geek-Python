# Задание 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
# Подсказка: использовать функцию range() и генератор.
start_number = 20
end_number = 240

condition_1 = 20
condition_2 = 21


print([el for el in range(start_number, end_number + 1) if el % condition_1 == 0 or el % condition_2 == 0])