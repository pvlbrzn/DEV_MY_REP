"""
Реализовать программу для нахождения индекса массы
тела человека. Пользователь вводит рост и вес с клавиатуры.
На выходе – ИМТ и пояснение к нему в зависимости от
попадания в тот или иной диапазон. Использовать обработку
исключений.
"""

while True:
    close = input('Для выхода из программы введите любой символ, '
                  'чтобы продолжить нажмите "Enter": ')
    if close == '':
        try:
            def bmi(h: float, w: float):
                """
                Функция находит ИМТ человека.
                :param h: float or int
                :param w: float or int
                """
                index = w / h ** h
                if index < 18.5:
                    print(f'ИМТ = {round(index)}. У вас дефицит веса.')
                elif 18.5 <= index <= 24.9:
                    print(f'ИМТ = {round(index)}. У вас нормальный вес.')
                elif 25 <= index <= 29.9:
                    print(f'ИМТ = {round(index)}. У вас избыточный вес.')
                elif 30 <= index <= 34.9:
                    print(f'ИМТ = {round(index)}. У вас ожирение I степени.')
                elif 35 <= index <= 39.9:
                    print(f'ИМТ = {round(index)}. У вас ожирение II степени.')
                elif 40 <= index:
                    print(f'ИМТ = {round(index)}. У вас ожирение III степени.')


            height = float(input('Введите Ваш рост в метрах: '))
            weight = float(input('Введите Ваш вес в килограммах: '))
            bmi(height, weight)

        except Exception as e:
            print('Вы ввели не то')
    else:
        break
