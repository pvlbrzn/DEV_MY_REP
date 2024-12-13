from lesson_12.lesson_task import models


def main():
    library = models.Library()
    library.load_from_file("library.json")

    while True:
        print("\nДобро пожаловать в библиотеку!")
        print("1. Показать доступные книги")
        print("2. Добавить книгу")
        print("3. Удалить книгу")
        print("4. Найти книги по автору")
        print("5. Взять книгу")
        print("6. Вернуть книгу")
        print("7. Состояние библиотеки (для Администратора)")
        print("8. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            books = library.list_available_books()
            if books:
                for book in books:
                    print(book)
            else:
                print("Нет доступных книг.")

        elif choice == "2":
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = input("Введите год издания книги: ")
            book_id = input("Введите ID книги: ")
            library.add_book(models.Book(title, author, year, book_id))
            print("Книга добавлена.")

        elif choice == "3":
            book_id = input("Введите ID книги, которую нужно удалить: ")
            library.remove_book(book_id)
            print("Книга удалена, если она существовала.")

        elif choice == "4":
            author = input("Введите имя автора: ")
            books = library.find_books_by_author(author)
            if books:
                for book in books:
                    print(book)
            else:
                print("Книги этого автора не найдены.")

        elif choice == "5":
            book_id = input("Введите ID книги, которую хотите взять: ")
            user = input("Введите ваше имя: ")
            if library.borrow_book(book_id, user):
                print("Книга успешно взята.")
            else:
                print("Книга недоступна или не существует.")

        elif choice == "6":
            book_id = input("Введите ID книги, которую хотите вернуть: ")
            if library.return_book_in_lib(book_id):
                print("Книга успешно возвращена.")
            else:
                print("Книга не была найдена среди занятых.")

        elif choice == "7":
            admin_pass = input("Введите пароль Администратора: ")
            if admin_pass == '12345':
                books = library.list_all_books()
                if books:
                    for book in books:
                        print(book)
                else:
                    print("Библиотека пустая")
            else:
                print('Неверный пароль')

        elif choice == "8":
            library.save_to_file("library.json")
            print("Состояние библиотеки сохранено. До свидания!")
            break

        else:
            print("Неверный выбор. Попробуйте ещё раз.")


if __name__ == "__main__":
    main()
