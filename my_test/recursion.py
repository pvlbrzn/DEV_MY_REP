data = [2, 4, 6, 9, 10, 13, 15]


def find_sum(arr: list) -> int:
    """
    Рекурсивная фанкция для поиска суммы элементов массива
    """
    if arr == []:
        return 0
    else:
        return arr[0] + find_sum(arr[1:])


def find_count(arr: list) -> int:
    """
    Рекурсивная функция для поиска количества элементов в массиве
    """
    if arr == []:
        return 0
    else:
        return 1 + find_count(arr[1:])


def find_max_el(list: list) -> int:
    """
    Рекурсивная функция поиска максимального элемента в списке
    """
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = find_max_el(list[1:])
    return list[0] if list[0] > sub_max else sub_max


def show():
    print(find_sum(data))
    print(find_count(data))
    print(find_max_el(data))


if __name__ == "__main__":
    show()
