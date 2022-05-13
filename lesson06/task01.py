# Задание 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора
# в режимы: красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно
# осуществляться только в указанном порядке (красный, желтый, зеленый). Проверить работу примера,
# создав экземпляр и вызвав описанный метод.

from time import sleep

class TrafficLight:
    __color: str

    def running(self):
        colours = ("\033[31mRed", "\033[33mYellow", "\033[32mGreen")
        while True:
            self.__color = colours[0]
            print(self.__color)
            sleep(7)
            self.__color = colours[1]
            print(self.__color)
            sleep(2)
            self.__color = colours[2]
            print(self.__color)
            sleep(10)


traffic_light = TrafficLight()
traffic_light.running()
