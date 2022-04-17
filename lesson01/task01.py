# Пункт 1. Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и
# строк и сохраните в переменные, выведите на экран.

string_var = "Привет! Покажу простую работу с числами. В частности - сумма двух чисел"
print(string_var)

digit_var1 = 4
digit_var2 = 5
digit_var3 = digit_var1 + digit_var2
print(f"Сумма чисел {digit_var1} и {digit_var2} равна числу {digit_var3}")

print("Теперь попробуте задать любые два числа для сложения")

digit_var1 = input("Введите первое число: ")
digit_var2 = input("Введите второе число: ")

while True:
    error = 0
    try:
        digit_var1 = float(digit_var1)
        digit_var2 = float(digit_var2)
        digit_var3 = digit_var1 + digit_var2
        print(f"Сумма заданных чисел {digit_var1} и {digit_var2} равна числу", "{:.2f}".format(digit_var3))
    except ValueError:
        error = 1
        print("Ошибка! Нужно ввести числовые значение. К примеру '3.4' и '5'.")
    if error == 0:
        break
    digit_var1 = input("Введите первое число повтроно: ")
    digit_var2 = input("Введите второе число повтроно: ")
# цикл реализован для повторного запроса данных в случае ввода некорректных