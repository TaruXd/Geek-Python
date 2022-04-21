# Пункт 6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

counter = 1
stop = False
check_price_error = "Ошибка! Цена товара должна быть положительным числом"
check_product_count_error = "Ошибка! Количество товара должно быть целым числом"
products_list = []
while not stop:
    product = input("Введите название товара: ")
    price = input("Введите цену товара: ")
    while True:
        error = 0
        try:
            price = float(price)
            if price <= 0:
                error = 1
                print(check_price_error)
        except ValueError:
            error = 1
            print(check_price_error)
        if error == 0:
            break
        price = float(input("Введите цену товара повторно: "))
    product_count = input("Введите количество товара: ")
    while True:
        error = 0
        try:
            product_count = int(product_count)
            if product_count < 0:
                error = 1
                print(check_product_count_error)
        except ValueError:
            error = 1
            print(check_product_count_error)
        if error == 0:
            break
        product_count = float(input("Введите количество товара повторно: "))
    count_uom = input("Введите единицы измерения товара: ")
# Создание словаря для нового продукта с заданными выше ключами
    new_product_dict = {"название": product, "цена": price, "количество": product_count, "ед": count_uom}
    product_tuple = (counter, new_product_dict)
# Добавление в список товаров нового товара
    products_list.append(product_tuple)
    counter += 1

# Запрос на добавление ещё одого нового товара. В случае n - выход из цикла создания списка товаров
    next_product = input("Добавить ещё товар? Y/N :")
    while next_product.lower() != "y" and next_product.lower() != "n":
        next_product = input("Добавить новый товар? Укажите один из ответов 'Y' или 'N': ")
    if next_product.lower() == "n":
        break
print("\nЗаданный список доваров:\n")
for pos in range(len(products_list)):
    print(products_list[pos])

# Создание пустых списков значений ключей по товарам
product_names_list = []
product_prices_list = []
product_counts_list = []
product_uoms_list = []

# Заполнение списков значений ключей по товарам
for pos in range(len(products_list)):
    product_tuple = products_list[pos]
    product_dict = product_tuple[1]
    product_names_list.append(product_dict.get("название"))
    product_prices_list.append(product_dict.get("цена"))
    product_counts_list.append(product_dict.get("количество"))
    product_uoms_list.append(product_dict.get("ед"))

# Создание словаря для аналитики товаров
products_analysis = {"название": product_names_list,
                     "цена": product_prices_list,
                     "количество": product_counts_list,
                     "ед": product_uoms_list}
print("\nАналитика товаров:\n")
print(products_analysis)