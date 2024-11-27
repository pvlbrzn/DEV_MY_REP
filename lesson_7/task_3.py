"""
 Дан список строк. С помощью filter() получить список
тех строк из исходного списка, которые являются
палиндромами (читаются в обе стороны одинаково, например,
’abcсba’)
"""

data = ['lol', 'pomidor', 'kek', 'chebyrek', 'око', 'шиш']


def is_palindrome(word: str) -> bool:
    if word[::] == word[::-1]:
        return True


new_list = list(filter(is_palindrome, data))
print(f'Дан список строк: {data}')
print(f'Список строк-палиндромов: {new_list}')
