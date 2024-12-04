"""
В файл записано некоторое содержимое (буквы,
цифры, пробелы, специальные символы и т.д.). Числом
назовём последовательность цифр, идущих подряд. Вывести
сумму всех чисел, записанных в файле.
 Входные данные: 123 ааа456 1x2y3z 4 5 6
 Выходные данные: 600
"""

import re


def find_sum_nums(some_file):
    """Функция находит сумму всех чисел в случайном наборе текста и цифр"""
    with open(f'{some_file}', 'r', encoding='utf-8') as file:
        data = file.read()
    nums_str = re.findall(r'\d+', data)
    return sum(list(map(lambda x: int(x), nums_str)))


my_file = 'some_file.txt'
print(f'Сумма всех чисел из файла {my_file} '
      f'равна {find_sum_nums(my_file)}')
