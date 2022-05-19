# Задание 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин,
# расположенных в виде прямоугольной схемы.
# Примеры матриц: см. в методичке.
#
# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов
# класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент
# первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    my_matrix: list

    def __init__(self, my_matrix: list):
        if isinstance(my_matrix, str) or isinstance(my_matrix, bool):
            raise Exception("Ошибка! Входным параметром класса Matrix должна быть прямоугольная матрица")
        else:
            size = len(my_matrix[0])
            for x in range(len(my_matrix)):
                if len(my_matrix[x]) == size:
                    pass
                else:
                    raise Exception("Ошибка! Входным параметром класса Matrix должна быть прямоугольная матрица")

            self.my_matrix = my_matrix

    def __str__(self):
        result = ""
        for x in range(len(self.my_matrix)):
            for y in range(len(self.my_matrix[x])):
                if y < len(self.my_matrix[x])-1:
                    result += str(self.my_matrix[x][y]) + " "
                else:
                    result += str(self.my_matrix[x][y]) + "\n"
        return result

    def __add__(self, other):
        if isinstance(other, Matrix):
            if len(self.my_matrix) == len(other.my_matrix):
                new_matrix = []
                for x in range(len(self.my_matrix)):
                    row = []
                    if len(self.my_matrix[x]) != len(other.my_matrix[x]):
                        return "Матрицы должны быть одинаковой размерности"
                    else:
                        for y in range(len(self.my_matrix[x])):
                            if isinstance(self.my_matrix[x][y], int) and isinstance(other.my_matrix[x][y], int):
                                new_element = self.my_matrix[x][y] + other.my_matrix[x][y]
                                row.append(new_element)
                            else:
                                row.append("".join([str(self.my_matrix[x][y]), str(other.my_matrix[x][y])]))
                    new_matrix.append(row)
                return new_matrix
            else:
                return "Матрицы должны быть одинаковой размерности"
        else:
            return "Складывать можно только объекты класса Matrix"



matrix_1 = Matrix([[1, 2, 3], [4, 5, "nd"]])
matrix_2 = Matrix([[1, 2, 3], [4, 5, 6]])
print("Матрица 1:")
print(matrix_1)
print("Матрица 2:")
print(matrix_2)

matrix_3 = Matrix(matrix_1 + matrix_2)
print("Сумма матриц (поэлементное сложение):")
print(matrix_3)


