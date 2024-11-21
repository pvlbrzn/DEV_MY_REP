"""
Реализовать алгоритм бинарного поиска по сдвинутому списку
отсортированных чисел (например, дан список [5, 6, 7, 1, 2, 3, 4])
"""

data = [5, 6, 7, 1, 2, 3, 4]
print(f'Дан сдвинутый список {data}, в котором необходимо '
      f'реализовать бинарный поиск')
b = int(input('Введите число: '))

left = 0
right = len(data) - 1

while left <= right:
    mid = (left + right) // 2
    if data[mid] == b:
        print(f'Ваше число находится в списке под индексом: {mid}')
        break
    if data[left] <= data[right]:  # Сортирован левый
        if data[left] <= b <= data[mid]:
            right = mid - 1  # Ищем в нем
        else:
            left = mid + 1  # Ищем в правом
    else:
        if data[mid] <= b <= data[right]:
            left = mid + 1
        else:
            right = mid - 1
