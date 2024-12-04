"""
В текстовый файл построчно записаны фамилия и имя
учащихся класса и оценка за контрольную. Вывести на экран
всех учащихся, чья оценка меньше трёх баллов.
"""


def who_is_a_bad_student(some_file):
    with open(f'{some_file}', 'r', encoding='utf-8') as file:
        data = file.readlines()
    print('Контрольную провалили следующие ученики: ')
    for el in data:
        grade = int(el.split(' ')[-1])
        if grade < 3:
            print(el[0:-2])


who_is_a_bad_student('list_of_students.txt')
