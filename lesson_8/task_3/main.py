def check_file(name_f: str):
    """Функция проверки наличия файла"""
    with open(name_f, 'r') as file:
        res = file.readlines()
    return res


def number_of_lines(name_f: str):
    """Функция принимает файл и выводит количество строк в нем"""
    with open(name_f, 'r') as file:
        file_lines = file.readlines()
        # Отфильтруем заполненные строки
        empty_lines = list(filter(lambda x: x == '\n', file_lines))
        num_lines = len(file_lines)
        num_empty_lines = len(empty_lines)
    print(f'Количество строк в файле: {num_lines}')
    if num_empty_lines > 0:
        print(f'Из них количество пустых: {num_empty_lines}')


def number_of_words(name_f: str) -> int:
    """Функция принимает файл и возвращает количество слов в нем"""
    with open(name_f, 'r') as file:
        file_lines = file.readlines()
        num_words = 0
        for line in file_lines:
            num_words += len(line.split())
    return num_words


def average_len_of_words(name_f: str) -> int:
    """Функция принимает файл и находит среднюю длину слов"""
    with open(name_f, 'r') as file:
        file_lines = file.readlines()
        num_words = 0  # Счетчик слов
        num_letters = 0  # Счетчик букв
        for line in file_lines:
            num_words += len(line.split())
        # Отфильтруем пустые строки
        filled_lines = list(filter(lambda x: x != '\n', file_lines))
        for line in filled_lines:
            # Делаем строку только из букв
            only_letters = ''.join(i for i in line if i.isalpha())
            num_letters += len(only_letters)
        res = num_letters // num_words
    return res


def show(change):
    if change == 1:
        number_of_lines(name_file)
    elif change == 2:
        print(f'Количество слов в файле: {number_of_words(name_file)}')
    elif change == 3:
        print(f'Средняя длина слов в файле: {average_len_of_words(name_file)} букв')
    else:
        print("Такой операции не существует, попробуйте снова.")


while True:
    start = input('Программа для чтения и обработки файлов.\n'
                  'Чтобы продолжить нажмите "Enter", для выхода введите любой символ: ')
    if start == '':
        try:
            name_file = input('Введите название файла: ')
            check_file(name_file)
            print(f'Файл {name_file}, успешно найден! \n'
                  f'Чтобы узнать количество СТРОК в файле введите "1" \n'
                  f'Чтобы узнать количество СЛОВ в файле введите "2" \n'
                  f'Чтобы узнать Среднюю Длину Слов в файле введите "3"')
            choice = int(input('Выберите операцию: '))
        except (FileNotFoundError):
            print("Файл с указанным именем - НЕ НАЙДЕН\n"
                  "Проверьте имя файла и попробуйте еще раз!")
        except (TypeError, ValueError):
            print('Не корректный ввод')
        except (PermissionError):
            print("Создатель файла запретил доступ к нему!")
        else:
            show(choice)
        finally:
            print("Программа завершена. \n", "-" * 60, "\n")
    else:
        print('Цикл программы успешно завершен.')
        break
