"""
Программа с классом Sphere для представления сферы в трёхмерном пространстве.
Реализовать методы:
 ● конструктор, принимающий 4 числа: радиус и координаты центра сферы x, y, z.
 Если конструктор вызывается без аргументов, создать объект сферы с единичным радиусом
и центром в начале координат. Если конструктор вызывается только с радиусом,
создать объект с соответствующим радиусом и центром в начале координат;
 ● метод get_volume(), возвращающий число – объем шара, ограниченного текущей сферой;
 ● метод get_square(), возвращающий число – площадь внешней поверхности сферы;
 ● метод get_radius(), возвращающий число – радиус текущей сферы;
 ● метод get_center(), возвращающий кортеж с координатами центра сферы;
 ● метод set_radius(radius), принимает новое значение радиуса, меняет радиус
 текущей сферы и ничего не возвращает
 ● метод set_center(x, y, z), принимает новые значения для координат центра радиуса,
 меняет координаты текущей сферы и ничего не возвращает
 ● метод is_point_inside(x, y, z), который принимает координаты некой точки в трёхмерном
 пространстве и возвращает True или False в зависимости от того, находится ли точка внутри сферы
"""
from math import pi


class Sphere:

    def __init__(self, radius=1.0, x=0.0, y=0.0, z=0.0):
        """
        Инициализирует объект "сфера"
        :param radius: радиус сферы
        :param x, y, z: координаты центра сферы
        """
        self.radius = radius
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return (f"Сфера с радиусом: {self.radius}. Координаты центра сферы: "
                f"{self.x, self.y, self.z}")

    def get_volume(self) -> float:
        """Метод для нахождения объема сферы"""
        volume = 4 / 3 * pi * (self.radius ** 3)
        return round(volume, 2)

    def get_square(self) -> float:
        """Метод для нахождения площади поверхности сферы"""
        square = 4 * pi * (self.radius ** 2)
        return round(square, 2)

    def get_radius(self) -> float:
        """Метод возвращает значение радиуса"""
        return self.radius

    def get_center(self) -> tuple:
        """Метод возвращает кортеж из координат центра сферы"""
        return self.x, self.y, self.x

    def set_radius(self, radius):
        """
        Метод для изменения радиуса сферы
        :param radius: Значение нового радиуса
        """
        self.radius = radius
        print(f'Радиус сферы изменен. Новый радиус равен {self.radius} см')

    def set_center(self, x, y, z):
        """Метод для изменения координат центра сферы"""
        self.x = x
        self.y = y
        self.z = z
        print(f'Координаты центра сферы изменены. Центр сферы перемещен в '
              f'координаты {self.x, self.y, self.z}')

    def is_point_inside(self, x, y, z):
        """Метод принимает точку в пространстве и проверяет,
        находится ли она в границах заданной сферы"""
        if ((self.x - x) ** 2) + ((self.y - y) ** 2) + ((self.z - z) ** 2) <= self.radius ** 2:
            return True
        else:
            return False


some_sphere = Sphere()
print(some_sphere)
print(f"Объем сферы равен {some_sphere.get_volume()} см/куб")
print(f"Площадь поверхности сферы равна {some_sphere.get_square()} см/кв")
print(f"Радиус сферы равен {some_sphere.get_radius()} см")
print(f"Координаты центра сферы: {some_sphere.get_center()}")
some_sphere.set_radius(5)
some_sphere.set_center(1, 5, 3)
print(some_sphere)
print(some_sphere.is_point_inside(5, 6, 7))
print(some_sphere.is_point_inside(2, 7, 4))
