import time
from random import randint

"""
Сделать декоратор, который измеряет время, 
затраченное на выполнение декорируемой функции.
"""


def time_logger(funk):
    """
    Декоратор считает время работы функции
    :param funk: принимает функцию
    :return: возвращает функцию и время ее работы
    """

    def _executor(data):
        start_time = time.time()
        res = funk(data)
        end_time = time.time() - start_time
        print(f'Время работы функции = {end_time:.5f} сек')
        return res

    return _executor


@time_logger
def norm_sort(data: list) -> list:
    """
    Функция сортирует и выводит полученный список
    :param data: list of int or float value
    :return: sorted list
    """
    print(data)
    data.sort()
    print(data)
    return data


my_list = [randint(-1000, 10000) for _ in range(10000)]
norm_sort(my_list)
