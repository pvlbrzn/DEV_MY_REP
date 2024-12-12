import json


class Book:
    def __init__(self, title, author, year, book_id):
        self.title = title
        self.author = author
        self.year = year
        self.book_id = book_id
        self.is_available = True
        self.user_book = None

    def borrow(self, user):
        if self.is_available:
            self.is_available = False
            self.user_book = user
            return True
        return False

    def return_book(self):
        self.is_available = True
        self.user_book = None

    def __str__(self):
        if self.is_available:
            status_book = "Книга доступна"
        else:
            status_book = f"Книгу забрал {self.user_book}"
        return f"{self.title}, {self.author}, [ID: {self.book_id}] - {status_book}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        """Метод для добавления книги"""
        self.books.append(book)

    def remove_book(self, book_id):
        """Метод для удаления книги"""
        for book in self.books:
            if book.book_id == book_id:
                print(f"Книга {book.title} удалена из библиотеки")
                self.books.remove(book)
                break

    def find_books_by_author(self, author):
        """Метод возвращает список книг автора"""
        return [book for book in self.books if book.author.lower() == author.lower()]

    def list_available_books(self):
        """Метод возвращает список доступных книг"""
        return [book for book in self.books if book.is_available]

    def borrow_book(self, book_id, user):
        """Метод для получения пользователем книги из библиотеки"""
        for book in self.books:
            if book.book_id == book_id and book.is_available:
                return book.borrow(user)
        return False

    def return_book_in_lib(self, book_id):
        """Метод для возврата книги"""
        for book in self.books:
            if book.book_id == book_id and not book.is_available:
                book.return_book()
                return True
        return False

    def save_to_file(self, filename):
        with open(filename, 'w', encoding="utf-8") as json_file:
            data = [book.__dict__ for book in self.books]
            json.dump(data, json_file, ensure_ascii=False, indent=4)

    def load_from_file(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                self.books = []
                for book_data in data:
                    book = Book(book_data['title'], book_data['author'], book_data['year'], book_data['book_id'])
                    book.is_available = book_data['is_available']
                    self.books.append(book)
        except FileNotFoundError:
            pass
