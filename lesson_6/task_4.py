"""
Программа получает на вход два числа и находит их НОД.
"""

print('Программа находит НОД введенных чисел')
a = int(input('Введите первое число (целое, больше нуля): '))
b = int(input('Введите второе число (целое, больше нуля): '))


def search_nod(num_a: int, num_b: int) -> int:
    """Функция поиска НОД двух чисел.

    Для поиска НОД используется 'алгоритм Евклида'
    """
    while num_a != 0 and num_b != 0:
        if num_a > num_b:
            num_a = num_a % num_b
        else:
            num_b = num_b % num_a
    return num_a + num_b


print(f'НОД чисел {a} и {b} = {search_nod(a, b)}'
      if a and b > 0 else 'Вы ввели что-то не то')
