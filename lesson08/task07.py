# Задание 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
# создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class ComplexNumber:

    real: float
    imag: float

    def __init__(self, real: float, imag: float):
        assert not isinstance(real, float) or not isinstance(imag, float), "Реальная и мнимая части должны быть действительными числами"
        self.real = real
        self.imag = imag

    def __add__(self, other: object):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real + other.real, self.imag + other.imag)

    # ac + ad i + b c i — b d
    def __mul__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real * other.real - self.imag * other.imag,
                                 self.real * other.imag + self.imag * other.real)

    def __str__(self):
        # result = ""
        # if self.real < 0:
        #     result += "- " + str(abs(self.real))
        # else:
        #     result += str(abs(self.real))
        # if self.imag < 0:
        #     result += " - " + str(abs(self.imag)) + "i"
        # else:
        #     result += " + " + str(abs(self.imag)) + "i"
        # return result
        return f"{self.real}{self.imag}i"

num_1 = ComplexNumber(1, -3)
num_2 = ComplexNumber(-3, -8)
print(f"Первое число: {num_1}")
print(f"Действительная часть первого числа: {num_1.real}")
print(f"Мнимая часть первого числа: {num_1.imag}")
print(f"Второе число: {num_2}")
print(f"Сложение чисел: {num_1 + num_2}")
print(f"Умножение чисел: {num_1 * num_2}")

