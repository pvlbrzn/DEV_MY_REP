"""
Реализовать вывод последовательности чисел Фибоначчи
(1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 …),
где каждое следующее число является суммой двух предыдущих.
"""

print("Последовательность Фибоначчи - такая последовательность, "
      "где каждое следующее число является суммой двух предыдущих.")
row_length = int(input('Введите количество чисел для ряда Фибоначчи: '))
row = [1, 1]

for i in range(2, row_length):
    new_el = row[-1] + row[-2]
    row.append(new_el)

print(row[0:row_length])
