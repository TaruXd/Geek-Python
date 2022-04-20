# Пункт 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

# Не до конца понятна логика требования "должен разместиться после них",
# но реализовал так, что результат получается тот же.
my_list = [7, 5, 3, 3, 2]
new_element = input("Введите новый элемент рейтинга: ")
check_element_error = "Ошибка! Новый элемент рейтинга должен быть натуральным числом"
while True:
    error = 0
    try:
        new_element = int(new_element)
        if new_element <= 0:
            error = 1
            print(check_element_error)
        else:
            my_list.append(new_element)
            my_list.sort()
            my_list.reverse()
            print(my_list)
    except ValueError:
        error = 1
        print(check_element_error)
    if error == 0:
        break
    new_element = int(input("Введите новый элемент рейтинга повторно: "))