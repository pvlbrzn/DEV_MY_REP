import time
from random import randint


def time_logger(func):
    def inner(some_list):
        start_time = time.perf_counter()  # Используем более точный таймер
        res = func(some_list)
        end_time = time.perf_counter() - start_time
        print(f'Время работы функции {func.__name__} = {end_time:.10f} секунд')  # Выводим с высокой точностью
        return res

    return inner


def quicksort(some_list):
    if len(some_list) < 2:
        return some_list
    else:
        pivot = some_list[0]
        less = [i for i in some_list[1:] if i <= pivot]
        greater = [i for i in some_list[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


@time_logger
def py_sort(some_list):
    some_list.sort()
    return some_list


@time_logger
def puz_sort(some_list):
    n = len(some_list) - 1
    while n > 0:
        for i in range(n):
            if some_list[i] > some_list[i + 1]:
                # equivalent some_list[i], some_list[i+1] = some_list[i+1], some_list[i]
                some_list[i] = some_list[i] + some_list[i + 1]
                some_list[i + 1] = some_list[i] - some_list[i + 1]
                some_list[i] = some_list[i] - some_list[i + 1]
        else:
            n -= 1
    return some_list


@time_logger
def my_sort(some_list):
    for i in range(len(some_list)):
        for j in range(i + 1, len(some_list)):
            if some_list[j] < some_list[i]:
                some_list[j], some_list[i] = some_list[i], some_list[j]
    return some_list


my_list = [randint(-1000, 1000) for i in range(1000)]

timed_quicksort = time_logger(quicksort)
sorted_data = timed_quicksort(my_list)
puz_sort(my_list)
my_sort(my_list)
py_sort(my_list)
