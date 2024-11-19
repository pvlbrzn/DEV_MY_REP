from lesson_6.martix import make_matrix

""" 
Реализовать функцию, которая находит сумму элементов 
на главной диагонали и сумму элементов на побочной 
диагонали (матрица M x N).
"""


def sum_main_diagonal(mtrx: list) -> int:
    """Функция находит сумму элементов на главной диагонали матрицы"""
    sum_main_di = 0
    for row in range(len(mtrx)):
        for col in range(len(mtrx[row])):
            if row == col:  # У элементов на главной диагонали оба индекса равны
                sum_main_di += mtrx[row][col]
    return sum_main_di


def sum_side_diagonal(mtrx: list) -> int:
    """Функция находит сумму элементов на побочной диагонали матрицы"""
    sum_side_di = []
    n = len(mtrx)  # Размер нашей матрицы
    for row in range(len(mtrx)):
        for col in range(len(mtrx[row])):
            if mtrx[row][n - row - 1] not in sum_side_di:
                sum_side_di.append(mtrx[row][n - row - 1])
    return sum(sum_side_di)


row_m = int(input('Введите количество строк в матрице (от 1 до 15): '))
col_m = int(input('Введите количество столбцов в матрице (от 1 до 15): '))
if 15 >= row_m and col_m >= 1:
    matrix = make_matrix(row_m, col_m)
    print(f'Сгенерирована матрица {row_m} x {col_m} '
          f'случайно заполненная числами:', *matrix, sep='\n')
    print(f'Сумма элементов на главной диагонали = {sum_main_diagonal(matrix)}')
    print(f'Сумма элементов на побочной диагонали = {sum_side_diagonal(matrix)}')

else:
    print('Вы ввели число не из представленного диапазона =(')
