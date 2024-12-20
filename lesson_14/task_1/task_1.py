"""
Представим, что у нас есть таблица "Employees" с
полями "Name", "Position", "Department", "Salary".
 ● Создайте таблицу "Employees" с указанными полями.
 ● Вставьте в таблицу несколько записей с информацией о
сотрудниках вашей компании.
 ● Измените данные в таблице для каких-то сотрудников.
Например, изменим должность одного из сотрудников на
более высокую.
 ● Добавьте новое поле "HireDate" (дата приема на работу) в
таблицу "Employees".
 ● Добавьте записи о дате приема на работу для всех
сотрудников.
 ● Найдите всех сотрудников, чья должность "Тимлид".
 ● Найдите всех сотрудников, у которых зарплата больше
5000 долларов.
 ● Найдите всех сотрудников, которые работают в отделе
"Парсинг".
 ● Найдите среднюю зарплату по всем сотрудникам.
 ● Удалите таблицу "Employees".
 * в качестве задания с повышенным уровнем сложности
можете реализовать пункты 6-9 в рамках хранимой функции
"""

import sqlite3

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('Employees.db')
cursor = connection.cursor()

# Создаем таблицу Employees
cursor.execute('''
CREATE TABLE IF NOT EXISTS Employees (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
position TEXT NOT NULL,
department TEXT NOT NULL,
salary REAL NOT NULL
)
''')

# Добавляем новых работников
employees_data = [
    ("Иван Иванов", "Python разработчик", "Парсинг", 500),
    ("Петя Петров", "Фронтэнд разработчик", "отдел разработки", 620.50),
    ("Миша Сидоров", "Тимлид", "отдел разработки", 10000),
    ("Никита Никитин", "Джун", "стажировка", 200)
]

for employees in employees_data:
    cursor.execute('''
    INSERT INTO Employees (name, position, department, salary)
    VALUES (?, ?, ?, ?)
    ''', employees)

connection.commit()

# Проверка данных в таблице
print("\nВсе работники в базе:")
cursor.execute('SELECT * FROM Employees')
for row in cursor.fetchall():
    print(row)

# Обновляем должность работника "Никита Никитин"
cursor.execute('UPDATE Employees SET position = "Джун+", salary = 450 WHERE name = "Никита Никитин"')
connection.commit()
print("\nНикита Никитин повышен до позиции Джун+")

# Добавление нового поля HireDate
cursor.execute('ALTER TABLE Employees ADD COLUMN HireDate TEXT')

# Добавление данных о дате приема на работу
hire_dates = [
    ("2020-05-15", 1),
    ("2018-03-10", 2),
    ("2019-07-20", 3),
    ("2021-11-01", 4)
]
cursor.executemany('UPDATE Employees SET HireDate = ? WHERE id = ?', hire_dates)
connection.commit()
print("\nДаты приема на работу обновлены.")
cursor.execute('SELECT * FROM Employees')
for row in cursor.fetchall():
    print(row)

# Найдите всех сотрудников, чья должность "Тимлид"
print('\nВсе работники на должности "Тимлид":')
cursor.execute('SELECT * FROM Employees WHERE position = "Тимлид"')
for row in cursor.fetchall():
    print(row)

# Найдите всех сотрудников, у которых зарплата больше 5000 долларов.
print('\nРаботники у которых ЗП выше 5000:')
cursor.execute('SELECT * FROM Employees WHERE salary > 5000')
for row in cursor.fetchall():
    print(row)

# Найдите всех сотрудников, которые работают в отделе "Парсинг".
print('\nРаботники в отделе "Парсинг":')
cursor.execute('SELECT * FROM Employees WHERE department = "Парсинг"')
for row in cursor.fetchall():
    print(row)

# Найти среднюю зарплату
cursor.execute('SELECT AVG(salary) AS AverageSalary FROM Employees')
average_salary = cursor.fetchone()[0]
print(f"\nСредняя зарплата всех сотрудников: {average_salary:.2f}")

# Удалить таблицу Employees
cursor.execute('DROP TABLE IF EXISTS Employees')
print("\nТаблица 'Employees' удалена.")
connection.commit()

connection.close()
