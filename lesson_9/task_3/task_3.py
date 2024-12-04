"""
Напишите программу, которая считывает текст из
файла (в файле может быть больше одной строки) и выводит
в новый файл самое часто встречаемое слово в каждой
строке и число – счётчик количества повторений этого слова
в строке.
"""

from collections import Counter
import re


def find_most_common_words(input_file: str) -> None:
    """
    Считывает текст из файла, определяет самое часто встречающееся слово
    в каждой строке и записывает результат в новый файл.
    """
    with open(input_file, 'r', encoding='utf-8') as file:

        for line_number, line in enumerate(file, start=1):
            # Разделяем строку на слова, убирая знаки препинания
            words = re.findall(r'\b\w+\b', line.lower())

            if not words:
                continue

            # Количество слов
            word_counts = Counter(words)

            # Находим самое частое слово и его количество
            most_common_word, count = word_counts.most_common(1)[0]

            with open('save_res.txt', 'a', encoding='utf-8') as save_file:
                save_file.write(f'В строке "{line_number}": слово "{most_common_word}" '
                                f'повторяется {count} раз\n')


input_file_path = "text.txt"
find_most_common_words(input_file_path)
