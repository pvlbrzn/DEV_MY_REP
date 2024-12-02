"""
Есть папка, в которой лежат файлы с разными расширениями.
Программа должна:
 1) Вывести имя вашей ОС;
 2) Вывести путь до папки, в которой вы находитесь;
 3) Рассортировать файлы по расширениям, например, для текстовых файлов создается папка,
в неё перемещаются все файлы с расширением .txt, то же самое для остальных расширений;
 4) После рассортировки выводится сообщение типа «в папке с текстовыми файлами перемещено
5 файлов, их суммарный размер - 50 гигабайт»;
 5) Как минимум один файл в любой из получившихся поддиректорий переименовать.
Сделать вывод сообщения типа «Файл data.txt был переименован в some_data.txt»;
 6) Программа должна быть кроссплатформенной – никаких хардкодов с именем диска и слэшами.
"""

import os
import platform


def selector():
    """Красивый разделитель"""
    print('*' * 60)


def make_folders(main_path):
    """Функция создает новые папки для сортировки файлов

    Названия папки это расширение файла
    """
    files_in_folder = [f for f in os.listdir(main_path) if os.path.isfile(f)]
    extensions = []  # Из списка расширений создадим названия новых папок
    for file in files_in_folder:
        extension = file.split('.')[-1]
        if extension != 'py':
            extensions.append(extension)
    for el in extensions:
        new_path = os.path.join(f'{main_path}', f'{el}')
        if not os.path.exists(new_path):
            os.mkdir(new_path)


def sort_file(main_path):
    """Функция сортирует файлы по папкам в соответствии с их расширением"""
    # Список путей к файлам
    try:
        file_paths = [f.path for f in os.scandir(main_path) if not f.is_dir()]
        for file_path in file_paths:
            extension = file_path.split('.')[-1]  # Расширение (имя новой папки)
            file_name = file_path.split('\\')[-1]  # Имя файла
            new_path = os.path.join(f'{main_path}', f'{extension}', f'{file_name}')
            if extension != 'py':
                print(f'Файл: {file_name} перемещен в папку: {extension}')
                os.rename(file_path, new_path)
                file_stat = os.stat(new_path)
                size_file = file_stat.st_size
                print(f'Размер файла {size_file} Байт')
    finally:
        print("Все файлы рассортированы по папкам!")


def show():
    print('Задача 1: Вывести имя своей ОС.')
    os_name = platform.system()
    print(f'Моя операционная система {os_name}')
    selector()
    print('Задача 2: Вывести путь.')
    print("Текущий каталог:", os.getcwd())
    selector()
    print('Задача 3: Рассортировать файлы по папкам.')
    some_path = os.getcwd()
    make_folders(some_path)
    sort_file(some_path)


show()
