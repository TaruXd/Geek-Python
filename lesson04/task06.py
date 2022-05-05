# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
#
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.

from itertools import count
from itertools import cycle

start_number = 11
step = 1
stop_condition = 20

my_list = ["One", "Two", "Three", "Four", "Five"]
element = cycle(my_list)

# Решил второй итератор вставить внутрь первого, где 1-й счетчик, а 2-й повторяющиеся элементы
for x in count(start_number, step):
    if x > stop_condition:
        break
    print(f"Значение итератора count - {x}")
    print(f"Значение итератора cycle - {next(element)}")

