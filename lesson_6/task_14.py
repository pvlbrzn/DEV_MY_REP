from random import randint

"""
Дана матрица M x N. Исходная матрица состоит из нулей и единиц. 
Реализовать функцию, которая добавит к матрице ещё один столбец, 
делающий количество единиц в соответствующей строке чётным.
"""


def make_matrix(m: int, n: int) -> list:
    """Функция создает матрицу случайно заполненную 0 и 1"""
    mtrx = [[randint(0, 1) for _ in range(n)] for _ in range(m)]
    return mtrx


def matrix_add_col(mtrx: list) -> list:
    """
    Функция добавляет столбик к матрице который
    делает сумму элементов строки четной
    """
    for row in range(len(mtrx)):
        # Проверяем сумму элементов строки на чет/нечет
        if sum(mtrx[row]) % 2 == 0:
            mtrx[row].append(0)  # Чет, добавляем ноль
        else:
            mtrx[row].append(1)  # Нечет, добавляем 1
    return mtrx


row_m = int(input('Введите количество строк в матрице (от 1 до 15): '))
col_m = int(input('Введите количество столбцов в матрице (от 1 до 15): '))
if 15 >= row_m and col_m >= 1:
    matrix = make_matrix(row_m, col_m)
    print(f'Сгенерирована матрица {row_m} x {col_m} '
          f'случайно заполненная 0 и 1:', *matrix, sep='\n')
    new_matrix = matrix_add_col(matrix)
    print('Матрица с добавленным столбиком: ', *new_matrix, sep='\n')
else:
    print('Вы ввели число не из представленного диапазона =(')
