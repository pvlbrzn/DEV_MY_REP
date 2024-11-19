from lesson_6.task_7 import make_matrix
from lesson_6.task_8 import m1, n1

"""
Реализовать функцию, которая находит сумму элементов 
матрицы (матрица M x N). Определить, какую долю в общей сумме 
(процент) составляет сумма элементов каждого столбца.
"""


def sum_matrix(matr: list) -> int:
    """Функция возвращает сумму всех элементов матрицы"""
    sum_el = 0
    for i in range(len(matr)):
        for j in range(len(matr[i])):
            sum_el += matr[i][j]
    return sum_el


def find_share_sum_col(matr, sum_el):
    """Функция возвращает долю суммы столбца матрицы от общей суммы"""
    # Создадим список в котором сохраним суммы столбцов
    sum_col_list = list(map(sum, zip(*matr)))
    share_sum_col = []  # Пустой список, чтобы сохранить там доли столбцов от суммы
    # Цикл в результате которого получим список долей столбцов
    for _ in sum_col_list:
        sh = _ / sum_el * 100
        share_sum_col.append(sh)
    return share_sum_col


matrix1 = make_matrix(m1, n1)
print(f'Сгенерированная ранее матрица {matrix1}')
print(f'Сумма элементов матрицы = {sum_matrix(matrix1)}')
share = find_share_sum_col(matrix1, sum_matrix(matrix1))
for _ in range(len(share)):
    print(f'Отношение суммы элементов {_ + 1} '  
          f'колонки к сумме элементов матрицы = {round(share[_], 2)} %')
