from lesson_6.martix import make_matrix

"""
Реализовать функцию, которая перемножает 
элементы каждого столбца матрицы с соответствующими 
элементами K-го столбца (матрица M x N).
"""


def multiply_by_col(mtrx: list, k: int) -> list:
    """
    Функция для умножения элементов матрицы выбранного столбика
    на элементы матрицы оставшихся столбиков
    """
    for row in range(len(mtrx)):
        for col in range(len(mtrx[row])):
            if col != k:
                mtrx[row][col] *= mtrx[row][k]
    return mtrx


matrix = make_matrix(5, 5)
print('Дана матрица 5х5 заполненная случайными числами: ', *matrix, sep='\n')
k_col = int(input('Выберите на какой столбик элементов перемножить (от 1 до 5): '))
if k_col <= 5:
    print(f'После умножения элементов {k_col} столба на элементы оставшихся столбов,'
          f'получилась матрица:', *multiply_by_col(matrix, k_col - 1), sep='\n')
else:
    print('Вы ввели что-то не то')
