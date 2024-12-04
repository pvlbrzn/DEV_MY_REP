"""
0. Есть данные в формате JSON – взять с диска с исходными данными.

1. Реализовать функцию, которая считает данные из исходного JSON-файла и преобразует их в формат CSV.

2. Реализовать функцию, которая сохранит данные в CSV-файл (данные должны сохраняться независимо от их
количества – если добавить в исходный JSON-файл ещё одного сотрудника, работа программы не должна
нарушаться).

3. Реализовать функцию, которая добавит информацию о новом сотруднике в JSON-файл. Пошагово вводятся все
необходимые данные о сотруднике, формируются данные для записи.

4. Такая же функция для добавления информации о новом сотруднике в CSV-файл.

5. Реализовать функцию, которая выведет информацию об одном сотруднике по имени. Имя для поиска вводится с
клавиатуры.

6. Реализовать функцию фильтра по языку: с клавиатуры вводится язык программирования, выводится список всех
сотрудников, кто владеет этим языком программирования.

7. Реализовать функцию фильтра по году: ввести с клавиатуры год рождения, вывести средний рост всех
сотрудников, у которых год рождения меньше заданного.

8. Программа должна представлять собой интерактив пользовательское меню с возможностью выбора
определённого действия (действия – функции из предыдущих пунктов + выход из программы). Пока
пользователь не выберет выход из программы, должен предлагаться выбор следующего действия.
"""

import json
import csv


def read_json(file_path: str) -> list:
    """
    Читает данные из JSON-файла и возвращает их в виде списка словарей.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def from_json_to_csv(input_file):
    with open(f'{input_file}', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    with open('employees.csv', 'w', encoding='utf-8') as csv_file:
        file_writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())
        file_writer.writeheader()
        file_writer.writerows(data)


def add_employee_to_json(json_file: str) -> None:
    """
    Добавляет нового сотрудника в JSON-файл.
    """
    new_employee = {
        "name": input("Введите имя сотрудника: "),
        "birthday": input("Введите дату рождения: "),
        "height": float(input("Введите рост (в см): ")),
        "weight": float(input("Введите вес (в кг): ")),
        "car": bool(input("Автомобиль (True/False): ")),
        "languages": input("Введите языки программирования через запятую: ").split(",")
    }
    with open(json_file, 'r', encoding='utf-8') as json_file_read:
        data = json.load(json_file_read)
    data.append(new_employee)
    with open(json_file, 'w', encoding='utf-8') as json_file_write:
        json.dump(data, json_file_write, indent=4)
    print("Новый сотрудник добавлен в JSON-файл.")


def add_employee_to_csv(csv_file: str) -> None:
    """
    Добавляет нового сотрудника в CSV-файл.
    """
    new_employee = {
        "name": input("Введите имя сотрудника: "),
        "birthday": input("Введите дату рождения: "),
        "height": float(input("Введите рост (в см): ")),
        "weight": float(input("Введите вес (в кг): ")),
        "car": bool(input("Автомобиль (True/False): ")),
        "languages": input("Введите языки программирования через запятую: ").split(",")
    }
    with open(csv_file, 'a', encoding='utf-8', newline='') as csv_file_write:
        writer = csv.DictWriter(csv_file_write, fieldnames=new_employee.keys())
        writer.writerow(new_employee)
    print("Сотрудник успешно добавлен в CSV.")


def find_employee_by_name(file_path: str, name: str) -> None:
    """
    Находит и выводит информацию о сотруднике по имени.
    """
    employees = read_json(file_path)
    for employee in employees:
        if employee['name'].lower() == name.lower():
            print(f"Информация о сотруднике {name}: {employee}")
            return
    print(f"Сотрудник с именем {name} не найден.")


def filter_by_language(json_file: str) -> None:
    """
    Выводит сотрудников, владеющих указанным языком программирования.
    """
    data = read_json(json_file)
    language = input("Введите язык программирования для фильтрации: ").strip().lower()
    filtered = [emp for emp in data if language in (lang.lower() for lang in emp['languages'])]
    if filtered:
        print(f"Сотрудники, владеющие языком {language}:")
        for emp in filtered:
            print(emp)
    else:
        print(f"Сотрудников, владеющих языком {language}, не найдено.")


def interactive_menu():
    """
    Интерактивное меню программы.
    """
    json_file = "employees.json"
    csv_file = "employees.csv"

    while True:
        print("\nМеню:")
        print("1. Преобразовать JSON в CSV")
        print("2. Добавить сотрудника в JSON")
        print("3. Добавить сотрудника в CSV")
        print("4. Найти сотрудника по имени")
        print("5. Фильтр по языку программирования")
        print("6. Выйти")
        choice = input("Выберите действие: ")

        if choice == "1":
            from_json_to_csv(json_file)
        elif choice == "2":
            add_employee_to_json(json_file)
        elif choice == "3":
            add_employee_to_csv(csv_file)
        elif choice == "4":
            name = input("Введите имя сотрудника для поиска: ")
            find_employee_by_name(json_file, name)
        elif choice == "5":
            filter_by_language(json_file)
        elif choice == "6":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор, попробуйте снова.")


interactive_menu()
