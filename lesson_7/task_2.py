"""
Задание 1
Дан список чисел. С помощью map() получить список,
где каждое число из исходного списка переведено в строку.
Пример: на входе – [1, 2, 3], на выходе – [‘1’, ‘2’, ‘3’]
"""

my_list = [1, 2, 3, 4, 5, 10]
new_list = list(map(lambda x: str(x), my_list))
print(f'Дан список чисел: {my_list}')
print(f'Используя функцию "map" получили список '
      f'строк: {new_list} \n')

"""
Задание 2
Дан список чисел. С помощью filter() получить список 
тех элементов из исходного списка, значение которых 
больше 0.
"""

some_list = [0, 2, -3, 5, -10, 4, -7, -4, 50, -25]
pos_list = list(filter(lambda x: x > 0, some_list))
print(f'Дан список чисел: {some_list}')
print(f'Используя функцию "filter" получили список '
      f'значений > 0: {pos_list}')