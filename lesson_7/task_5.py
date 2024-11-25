import functools

"""
Используя map() и reduce() посчитать площадь квартиры, 
имея на входе характеристики комнат квартиры.
"""

rooms = [{"name": "Kitchen", "length": 6, "width": 4},
         {"name": "Room 1", "length": 5.5, "width": 4.5},
         {"name": "Room 2", "length": 5, "width": 4},
         {"name": "Room 3", "length": 7, "width": 6.3}]


def get_area(data: dict) -> float or int:
    """
    Функция находит площадь комнаты из словаря
    :param data: dict
    :return: area of room: float or int
    """
    room_area = data.get('length') * data.get('width')
    return room_area


my_list = list(map(get_area, rooms))
for _ in range(len(my_list)):
    print(f'Площадь комнаты № {[_ + 1]} равна {my_list[_]} кв.м.')
apart_area = functools.reduce(lambda x, y: x + y, my_list)
print()
print(f'Общая площадь квартиры = {apart_area} кв.м')
