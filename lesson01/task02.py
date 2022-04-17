# Пункт 2. Пользователь вводит время в секундах. Переведите время в часы,
# минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

secs_amount = input("Введите количество секунд:")

while True:
    error = 0
    try:
        secs = int(secs_amount) % 60  # секунды
        mins = int(secs_amount) // 60 % 60  # минуты
        print(mins)
        hours = int(secs_amount) // 3600  # часы
        print("{:02d}".format(hours), ":", "{:02d}".format(mins), ":", "{:02d}".format(secs))
    except ValueError:
        error = 1
        print("Значение должно быть целым числом")
    if error == 0:
        break
    secs_amount = input("Введите количество секунд повторно:")
# цикл реализован для повторного запроса данных в случае ввода некорректных

