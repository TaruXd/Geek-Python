# Пункт 2. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.
import datetime

def user_info(first_name, last_name, birthday, city, email, phone):
    if first_name == "" or first_name == " ":
        print("Предупреждение! Не задано имя. Будет присвоено пустое занчение")
        first_name = None
    if last_name == "" or last_name == " ":
        print("Предупреждение! Не задана фамилия. Будет присвоено пустое занчение")
        last_name = None
    if city == "" or city == " ":
        print("Предупреждение! Не задан город. Будет присвоено пустое занчение")
        city = None
    try:
        birthday = int(birthday)
        if birthday > datetime.datetime.now().year or birthday < 1900:
            raise BaseException
    except BaseException:
        print("Предупреждение! Год рождени должен быть не раньше 1900 года и не больше текущего. Будет присвоено пустое занчение")
        birthday = None
    except:
        print("Предупреждение! Введен год рождения в неправильном формате. Будет присвоено пустое занчение")
        birthday = None
    try:
        if len(phone) != 11:
            raise BaseException
        phone = int(phone)
    except BaseException:
        print("Предупреждение! Номер телефона должен содержать 11 цифр. Будет присвоено пустое занчение")
        phone = None
    except:
        print("Предупреждение! Введен номер телефона в неправильном формате. Будет присвоено пустое занчение")
        phone = None
    try:
        if email.index("@") < 2 or email.index("@")+1 >= email.index(".") or email.index(".") == len(email):
            raise Exception
    except:
        email = None
        print("Предупреждение! Почта введена в неправильном формате. Будет присвоено пустое занчение")
    print(f"Имя: {first_name}, Фамилия: {last_name}, Год рождения: {birthday}, Город: {city}, Почта: {email}, Номер телефона: {phone}")

while True:
    user_info(birthday=input("Введите год рождения: "), city=input("Введите город: "), last_name=input("Введите фамилию: "),
                  phone=input("Введите номер телефона без +: "), first_name=input("Введите имя: "), email=input("Введите почту: "))
    next_attempt = None
    while next_attempt != "n" and next_attempt != "y":
        next_attempt = input("Повтороить ввод данных? Y/N ").lower()
    if next_attempt == "n":
        break