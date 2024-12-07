"""
Программа с классом Car. При инициализации объекта
ему должны задаваться атрибуты color, type и year.
Реализовать пять методов. Запуск автомобиля – выводит
строку «Автомобиль заведён». Отключение автомобиля
выводит строку «Автомобиль заглушен». Методы для
присвоения автомобилю года выпуска, типа и цвета.
"""


class Car:

    def __init__(self, color, type_car, year):
        self.color = color
        self.type_car = type_car
        self.year = year

    def start_engine(self):
        print(f"{self.color} {self.type_car} заведен")

    def stop_engine(self):
        print(f"{self.color} {self.type_car} заглушен")

    def set_color(self, color):
        self.color = color
        print(f'Автомобиль перекрашен в {self.color} цвет')

    def set_type_car(self, type_car):
        self.type_car = type_car
        print(f'Вин код авто перебит на марку {self.type_car}')

    def set_year(self, year):
        self.year = year
        print(f'Год выпуска авто перебит по документам на {self.year}')

    def __str__(self):
        return (f'Марка авто: {self.type_car}, год выпуска авто: {self.year}, '
                f'цвет авто: {self.color}')


car_1 = Car('Красный', 'Пежо 5008', '2019')
print(car_1)
car_1.start_engine()
car_1.stop_engine()
car_1.set_color('Синий')
print(car_1)
print("*" * 60)
car_2 = Car('Черный', 'Бумер', '1998')
print(car_2)
car_2.set_year('2005')
car_2.set_color('Белый')
print(car_2)
