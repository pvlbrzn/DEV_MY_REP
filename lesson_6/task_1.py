"""
Дан список чисел, отсортированных по возрастанию.
На вход принимается значение, равное одному из элементов списка.
Реализовать функцию, выполняющую рекурсивный алгоритм бинарного поиска,
на выходе программа должна вывести позицию искомого элемента в исходном списке.
"""


def binary_search_recursive(data: list, targ: int, left: int, right: int) -> int:
    """Функция бинарного поиска числа в отсортированном списке"""
    # Базовый случай: если диапазон пустой, элемент не найден
    if left > right:
        return -1  # Элемент не найден
    # Находим середину диапазона
    mid = (left + right) // 2
    # Проверяем, не является ли середина искомым элементом:
    if data[mid] == targ:
        return mid  # Элемент найден
    # Если элемент меньше среднего, ищем в левой половине
    elif targ < data[mid]:
        return binary_search_recursive(data, targ, left, mid - 1)
    # Если элемент больше среднего ищем в правой половине
    else:
        return binary_search_recursive(data, targ, mid + 1, right)


data_rec = [1, 2, 3, 5, 6, 7, 8, 9, 10]
print(f'Исходный список: {data_rec}')
target = int(input('Введите целое число от 1 до 10: '))
result = binary_search_recursive(data_rec, target, 0, len(data_rec) - 1)
print(f'Элемент {target}, найден в списке под индексом: '
      f'{result}' if result != -1 else 'Такого элемента в данном списке нет.')
