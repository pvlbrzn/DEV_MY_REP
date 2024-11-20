from lesson_6.martix import make_matrix

"""
Реализовать функцию, которая суммирует элементы 
каждой строки матрицы с соответствующими элементами L-й 
строки (матрица M x N). 
"""


def sum_by_row(mtrx: list, l_row: int) -> list:
    """
    Функция для сложения элементов матрицы выбранной строки
    с элементами матрицы оставшихся строк
    """
    for row in range(len(mtrx)):
        for col in range(len(mtrx[row])):
            if row != l_row:
                mtrx[row][col] += mtrx[l_row][col]
    return mtrx


matrix = make_matrix(5, 5)
print('Дана матрица 5х5 заполненная случайными числами: ', *matrix, sep='\n')
l_row_ch = int(input('Выберите с какой строкой элементов будем суммировать строки '
                     '(от 1 до 5): '))
if l_row_ch <= 5:
    print(f'После суммирования элементов {l_row_ch} строки на элементы остальных строк,'
          f'получилась матрица:', *sum_by_row(matrix, l_row_ch - 1), sep='\n')
else:
    print('Вы ввели что-то не то')
