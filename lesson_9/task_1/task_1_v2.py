"""
Этот скрипт сгенерировал чат GPT с учетом моего запроса.
Оставил его тут себе на память.
"""

from pathlib import Path
import shutil
import platform


def organize_files_in_directory(directory: Path) -> None:
    """
        Сортирует файлы в указанной директории по расширениям,
        создавая отдельные папки для каждого типа файлов.

        Исключает из сортировки файлы с расширением `.py`.

        :param directory: Путь к директории, в которой необходимо выполнить сортировку.
        """
    # Получаем имя ОС
    print(f"Операционная система: {platform.system()}")

    # Преобразуем путь в объект Path
    base_path = Path(directory).resolve()
    print(f"Текущая папка: {base_path}")

    # Создаем словарь для подсчета файлов и их размеров по расширениям
    file_summary = {}

    # Перебираем все элементы в папке
    for item in base_path.iterdir():
        # Пропускаем каталоги
        if item.is_dir():
            continue

        # Получаем расширение файла
        file_extension = item.suffix[1:]  # Убираем точку
        if not file_extension:  # Если файл без расширения
            file_extension = "no_extension"

        # Пропускаем файлы с расширением .py
        if file_extension == "py":
            continue

        # Создаем папку для расширения, если она не существует
        target_folder = base_path / file_extension
        target_folder.mkdir(exist_ok=True)

        # Перемещаем файл в соответствующую папку
        target_path = target_folder / item.name
        shutil.move(str(item), target_path)

        # Обновляем статистику
        file_size = target_path.stat().st_size
        if file_extension not in file_summary:
            file_summary[file_extension] = {'count': 0, 'size': 0}
        file_summary[file_extension]['count'] += 1
        file_summary[file_extension]['size'] += file_size

    # Выводим итоговую информацию
    for ext, stats in file_summary.items():
        size_in_gb = stats['size'] / (1024 ** 3)  # Переводим размер в гигабайты
        print(
            f"В папке с файлами типа {ext} перемещено {stats['count']} файлов, "
            f"их суммарный размер - {size_in_gb:.6f} ГБ.")


# Пример вызова программы
if __name__ == "__main__":
    folder_path = Path.cwd()  # Текущая рабочая директория
    organize_files_in_directory(folder_path)
