"""
Задача: Реализуйте генератор, который построчно считывает текстовый файл (ленивое чтение).

Напишите функцию file_reader(file_path), которая возвращает строки файла по одной.
Не загружайте весь файл в память.
Пример использования:
for line in file_reader("example.txt"):
    print(line.strip())
Дополнительно: Реализуйте генератор, который возвращает только строки, содержащие слово "Python".

"""


def file_reader(file_path: str, pointer: str):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            if pointer == 'all':
                for some_line in file:
                    yield some_line
            elif pointer == 'python':
                for some_line in file:
                    if 'Python' in some_line:
                        yield some_line
            else:
                print("pointer может быть 'all' or 'python'")
    except FileNotFoundError:
        print("Указанный файл не обнаружен!")


for line in file_reader("some_text.txt", "all"):
    print(line, end='')

print(end='\n\n')

for line in file_reader("some_text.txt", "python"):
    print(line, end='')

