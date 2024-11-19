"""
Программа получает на вход строку – сообщение и указание,
что нужно сделать: шифровать или дешифровать.
Реализовать две функции: первая шифрует заданное сообщение шифром Цезаря,
вторая расшифровывает. В зависимости от выбора пользователя
(шифровать или дешифровать) вызывается соответствующая функция,
результат выводится в консоль.
"""


def get_chip(message: str, lang: str, shift: int) -> str:
    """Функция шифрует сообщение шифром Цезаря"""
    alpha_ru = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    alpha_eu = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    res = ''
    if lang == 'рус':
        for i in message:
            place = alpha_ru.find(i)
            new_place = place + shift
            if i in alpha_ru:
                res += alpha_ru[new_place]
            else:
                res += i
    else:
        for i in message:
            place = alpha_eu.find(i)
            new_place = place + shift
            if i in alpha_eu:
                res += alpha_eu[new_place]
            else:
                res += i
    return res


def get_de_chip(message: str, lang: str, shift: int) -> str:
    """Функция расшифровывает сообщение шифром Цезаря"""
    alpha_ru = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    alpha_eu = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    res = ''
    if lang == 'рус':
        for i in message:
            place = alpha_ru.find(i)
            new_place = place - shift
            if i in alpha_ru:
                res += alpha_ru[new_place]
            else:
                res += i
    else:
        for i in message:
            place = alpha_eu.find(i)
            new_place = place - shift
            if i in alpha_eu:
                res += alpha_eu[new_place]
            else:
                res += i
    return res


while True:
    print('Программа для шифровки или дешифровки сообщения шифром Цезаря')
    close = input('Для выхода их программы введите "любой символ", '
                  'для продолжения нажмите "Enter": ')
    if len(close) > 0:
        print('Вы, вышли из программы!')
        break
    elif close == '':
        some_message = input("Введите текст: ").upper()
        lang_ch = input('Выберите язык рус/ин: ')
        shift_ch = int(input('Шаг шифровки: '))
        action = input('Для шифрования введите "ш", для расшифровки введите "р": ')
        if action in ['ш', 'Ш']:
            print(get_chip(some_message, lang_ch, shift_ch))
        elif action in ['р', 'Р']:
            print(get_de_chip(some_message, lang_ch, shift_ch))
print('*' * 60)
