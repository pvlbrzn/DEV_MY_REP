"""
1. "1984", George Orwell, 1949, доступна
2. "To Kill a Mockingbird", Harper Lee, 1960, доступна
3. "The Great Gatsby", F. Scott Fitzgerald, 1925, недоступна
4. "Moby Dick", Herman Melville, 1851, доступна
5. "War and Peace", Leo Tolstoy, 1869, недоступна
"""

import sqlite3

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('library.db')
cursor = connection.cursor()

# Создаем таблицу books
cursor.execute('''
CREATE TABLE IF NOT EXISTS books (
id INTEGER PRIMARY KEY,
title TEXT NOT NULL,
author TEXT NOT NULL,
year INTEGER,
available BLOB
)
''')

# Добавляем новые книги
books_data = [
    ("1984", "George Orwell", 1949, 1),
    ("To Kill a Mockingbird", "Harper Lee", 1960, 1),
    ("The Great Gatsby", "F. Scott Fitzgerald", 1925, 0),
    ("Moby Dick", "Herman Melville", 1851, 1),
    ("War and Peace", "Leo Tolstoy", 1869, 0)
]

for book in books_data:
    cursor.execute('''
    INSERT INTO books (title, author, year, available)
    VALUES (?, ?, ?, ?)
    ''', book)


# Сохраняем изменения и закрываем соединение
connection.commit()

# Проверка данных в таблице
print("\nВсе книги в базе:")
cursor.execute('SELECT * FROM books')
for row in cursor.fetchall():
    print(row)

# Найти книги, выпущенные после 1950 года
print("\nКниги, выпущенные после 1950 года:")
cursor.execute('''
SELECT * FROM books WHERE year > 1950
''')
for row in cursor.fetchall():
    print(row)

# Обновление доступности книги "The Great Gatsby" на "доступна"
cursor.execute('''
UPDATE books
SET available = 1
WHERE title = "The Great Gatsby"
''')
print("\nДоступность книги 'The Great Gatsby' обновлена.")

# Удаление книги "Moby Dick"
cursor.execute('''
DELETE FROM books
WHERE title = "Moby Dick"
''')
print("\nКнига 'Moby Dick' удалена.")
connection.commit()

# Проверка оставшихся книг
print("\nОставшиеся книги в базе:")
cursor.execute('''
SELECT * FROM books
''')
for row in cursor.fetchall():
    print(row)

# Удалить таблицу books
cursor.execute('DROP TABLE IF EXISTS books')
print("\nТаблица 'books' удалена.")
connection.commit()

connection.close()


