"""Модель книги с использованием валидации из отдельного модуля."""

import validation  # импорт функций валидации

class Book:
    """Класс, представляющий книгу в библиотеке."""
    total_books = 0  # атрибут класса: общее количество созданных книг

    def __init__(self, title: str, author: str, year: int, pages: int):
        """Конструктор с валидацией переданных данных."""
        self._title = None
        self._author = None
        self._year = None
        self._pages = None
        self._is_loaned = False  # по умолчанию книга доступна

        # Используем сеттеры для валидации через вызовы функций из validation
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages

        Book.total_books += 1

    # ----- Свойства (геттеры и сеттеры) -----
    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str):
        self._title = validation.validate_title(value)

    @property
    def author(self) -> str:
        return self._author

    @author.setter
    def author(self, value: str):
        self._author = validation.validate_author(value)

    @property
    def year(self) -> int:
        return self._year

    @year.setter
    def year(self, value: int):
        self._year = validation.validate_year(value)

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, value: int):
        self._pages = validation.validate_pages(value)

    @property
    def is_loaned(self) -> bool:
        """True, если книга выдана читателю."""
        return self._is_loaned

    # ----- Бизнес-методы, изменяющие состояние -----
    def issue(self):
        """Выдать книгу. Если уже выдана – возбуждается исключение."""
        if self._is_loaned:
            raise RuntimeError(f"Книга '{self._title}' уже выдана")
        self._is_loaned = True

    def return_book(self):
        """Вернуть книгу. Если не была выдана – возбуждается исключение."""
        if not self._is_loaned:
            raise RuntimeError(f"Книга '{self._title}' не была выдана")
        self._is_loaned = False

    # ----- Магические методы -----
    def __str__(self) -> str:
        """Краткое строковое представление для пользователя."""
        status = "выдана" if self._is_loaned else "доступна"
        return f"«{self._title}» {self._author} ({self._year}) – {status}"

    def __repr__(self) -> str:
        """Официальное строковое представление для разработчика."""
        return (f"Book(title='{self._title}', author='{self._author}', "
                f"year={self._year}, pages={self._pages}, is_loaned={self._is_loaned})")

    def __eq__(self, other) -> bool:
        """Две книги считаются равными, если совпадают название, автор и год."""
        if not isinstance(other, Book):
            return False
        return (self._title == other._title and
                self._author == other._author and
                self._year == other._year)