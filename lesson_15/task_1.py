from sqlalchemy import (
    create_engine, Column, Integer, String, ForeignKey
)
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

Base = declarative_base()


class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    books = relationship("Book", back_populates="author")


# Таблица books
class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'))
    publication_year = Column(Integer)
    author = relationship("Author", back_populates="books")
    sales = relationship("Sale", back_populates="book")


# Таблица sales
class Sale(Base):
    __tablename__ = 'sales'

    id = Column(Integer, primary_key=True, autoincrement=True)
    book_id = Column(Integer, ForeignKey('books.id'))
    quantity = Column(Integer, nullable=False)
    book = relationship("Book", back_populates="sales")


# Создаем базу данных
engine = create_engine('sqlite:///library.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


# Заполнение данных
def populate_data():
    # Добавляем авторов
    author1 = Author(first_name="Джордж", last_name="Оруэлл")
    author2 = Author(first_name="Рэй", last_name="Брэдбари")
    author3 = Author(first_name="Антон", last_name="Чехов")
    author4 = Author(first_name="Адитья", last_name="Бхаргава")
    author5 = Author(first_name="Лев", last_name="Толстой")
    session.add_all([author1, author2, author3, author4, author5])
    session.commit()

    # Добавляем книги
    book1 = Book(title="Скотный двор", author_id=author1.id, publication_year=1869)
    book2 = Book(title="451 градус по Фарингейту", author_id=author2.id, publication_year=1953)
    book3 = Book(title="Преступление и наказание", author_id=author3.id, publication_year=1866)
    book4 = Book(title="1984", author_id=author1.id, publication_year=1948)
    book5 = Book(title="Грокаем алгоритмы", author_id=author4.id, publication_year=2023)
    session.add_all([book1, book2, book3, book4, book5])
    session.commit()

    # Добавляем продажи
    sale1 = Sale(book_id=book1.id, quantity=150)
    sale2 = Sale(book_id=book2.id, quantity=120)
    sale3 = Sale(book_id=book3.id, quantity=200)
    sale4 = Sale(book_id=book4.id, quantity=180)
    session.add_all([sale1, sale2, sale3, sale4])
    session.commit()


# populate_data()

# INNER JOIN для получения списка всех книг и их авторов
inner_join_books_authors = session.query(Book.title, Author.first_name, Author.last_name).join(Author).all()

# LEFT JOIN для списка всех авторов и их книг
left_join_authors_books = session.query(Author.first_name, Author.last_name, Book.title).outerjoin(Book).all()

# RIGHT JOIN для списка всех книг и их авторов
right_join_books_authors = session.query(Book.title, Author.first_name, Author.last_name).outerjoin(Author).all()

# INNER JOIN для связывания таблиц authors, books и sales
inner_join_query = session.query(
    Book.title,
    Author.first_name,
    Author.last_name,
    Sale.quantity
).join(Author).join(Sale).all()

# LEFT JOIN для связывания таблиц authors, books и sales, чтобы получить список всех авторов, их книг
# и продаж (включая авторов без книг и книги без продаж)
left_join_query = session.query(
    Author.first_name,
    Author.last_name,
    Book.title,
    Sale.quantity
).select_from(Author).join(Book, isouter=True).join(Sale, isouter=True).all()

print("INNER JOIN (Books and Authors):", inner_join_books_authors)
print("LEFT JOIN (Authors and Books):", left_join_authors_books)
print("RIGHT JOIN (Books and Authors):", right_join_books_authors)
print("INNER JOIN (Books, Authors and Sales):", inner_join_query)
print("LEFT JOIN (Books, Authors and Sales):", left_join_query)
