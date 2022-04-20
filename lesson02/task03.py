# Пункт 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

# Не понял, как писать через list
# Через dict
month_dict = {
    1: "Зима", 2: "Зима", 12 : "Зима",
    3: "Весна", 4: "Весна", 5: "Весна",
    6: "Лето", 7: "Лето", 8: "Лето",
    9: "Осень", 10: "Осень", 11: "Осень"}
check_number_error = "Ошибка! Значение месяца должно быть от 1 до 12"
month_number = input("Введите порядковый номер месяца: ")
while True:
    error = 0
    try:
        month_number = int(month_number)
        if month_number not in month_dict.keys():
            error = 1
            print(check_number_error)
        else:
            print(month_dict.get(month_number))
    except ValueError:
        error = 1
        print(check_number_error)
    if error == 0:
        break
    month_number = int(input("Введите порядковый номер месяца повторно: "))