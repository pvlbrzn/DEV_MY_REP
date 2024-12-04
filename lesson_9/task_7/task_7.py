"""
Дан текстовый файл с несколькими строками.
Зашифровать шифром Цезаря, при этом шаг зависит от
номера строки: для первой строки шаг 1, для второй – 2 и т.д.
"""


def get_chip_for_string(input_file: str) -> None:
    """Функция принимает на вход файл и построчно шифрует его данные.
    Данные шифруются шифром 'Цезаря', где шаг шифровки соответствует
    номеру строки
    """
    data_for_write = []
    with open(f"{input_file}", 'r', encoding='utf-8') as file:
        for line_number, line in enumerate(file, start=1):
            res = ''
            #  В данном примере нам нужен только EN алфавит
            alpha_eu = ('ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
                        'abcdefghiklmnopqrstuvwxyzabcdefghigklmnopqrstuvwxyz')

            # Циклом смещаем буквы в словах на позицию равной номеру строки
            for ch in line:
                place = alpha_eu.find(ch)
                new_place = place + line_number
                if ch in alpha_eu:
                    res += alpha_eu[new_place]
                else:
                    res += ch

            # Добавляем зашифрованное слово в список для записи
            data_for_write.append(res)

            # Сохраняем результат в текстовый файл
            with open("save_res.txt", 'w', encoding='utf-8') as save_file:
                save_file.writelines(line for line in data_for_write)

    print(f"Результат шифрования файла: {input_file} "
          f"записан в файл: {save_file.name}")


get_chip_for_string('some_file.txt')
