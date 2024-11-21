from random import randint


def make_matrix(m: int, n: int) -> list:
    """Функция создает матрицу случайно заполненную числами"""
    mtrx = [[randint(0, 50) for _ in range(n)] for _ in range(m)]
    return mtrx
