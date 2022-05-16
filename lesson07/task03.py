# Задание 3. Реализовать программу работы с органическими клетками, состоящими из ячеек.
# Необходимо создать класс Клетка. В его конструкторе инициализировать параметр,
# соответствующий количеству ячеек клетки (целое число). В классе должны быть
# реализованы методы перегрузки арифметических операторов: сложение (add()),
# вычитание (sub()), умножение (mul()), деление (truediv()). Данные методы должны
# применяться только к клеткам и выполнять увеличение, уменьшение, умножение и
# целочисленное (с округлением до целого) деление клеток, соответственно.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно
# равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если
# разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется
# как произведение количества ячеек этих двух клеток.
# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется
# как целочисленное деление количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса
# и количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество
# ячеек между \n равно переданному аргументу. Если ячеек на формирование ряда
# не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n*****.

class Cell:
    cell_amount: int

    def __init__(self, cell_amount: int):
        assert cell_amount > 0, "Количество ячеек клетки должно быть положительным целым числом"
        self.cell_amount = cell_amount

    def __add__(self, other):
        if isinstance(other, Cell):
            return self.cell_amount + other.cell_amount
        else:
            raise TypeError("Сложение возможно только для объетов класса Cell")

    def __sub__(self, other):
        if isinstance(other, Cell):
            if self.cell_amount != other.cell_amount:
                return abs(self.cell_amount - other.cell_amount)
            else:
                raise ValueError("Вычитание возможно только в случае разного количества ячеек клеток")
        else:
            raise TypeError("Вычитание возможно только для объетов класса Cell")

    def __mul__(self, other):
        if isinstance(other, Cell):
            return self.cell_amount * other.cell_amount
        else:
            raise TypeError("Умножение возможно только для объетов класса Cell")

    def __truediv__(self, other):
        if isinstance(other, Cell):
            if self.cell_amount > other.cell_amount:
                return self.cell_amount // other.cell_amount
            else:
                return other.cell_amount // self.cell_amount
        else:
            raise TypeError("Деление возможно только для объетов класса Cell")

    @staticmethod
    def make_order(cell_object: 'Cell', collumns: int):
        order = ""
        for x in range(1, cell_object.cell_amount + 1):
            if x % collumns != 0:
                order += "*"
            else:
                if x == cell_object.cell_amount:
                    order += "*"
                else:
                    order += "*\n"
        print(order)




cell_1 = Cell(9)
cell_2 = Cell(5)

print(f"Количество ячеек в первой клетке: {cell_1.cell_amount}")
print(f"Количество ячеек во второй клетке: {cell_2.cell_amount}")

cell_3 = Cell(cell_1 + cell_2)
print(f"Сложение: {cell_3.cell_amount}")

cell_4 = Cell(cell_2 - cell_1)
print(f"Вычитание: {cell_4.cell_amount}")

cell_5 = Cell(cell_1 * cell_2)
print(f"Умножение: {cell_5.cell_amount}")

cell_6 = Cell(cell_1 / cell_2)
print(f"Деление: {cell_6.cell_amount}")

print("Ячейки первой клетки в заданном порядке:")
Cell.make_order(cell_1, 4)
