from abc import ABC, abstractmethod
import validation   # из ЛР-1

class Book(ABC):
    """Базовый класс для всех видов книг."""
    total_books = 0

    def __init__(self, title: str, author: str, year: int, pages: int):
        self._title = None
        self._author = None
        self._year = None
        self._pages = None
        self._is_loaned = False

        self.title = title
        self.author = author
        self.year = year
        self.pages = pages

        Book.total_books += 1

    # ----- Свойства (геттеры/сеттеры) -----
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, value):
        self._title = validation.validate_title(value)

    @property
    def author(self):
        return self._author
    @author.setter
    def author(self, value):
        self._author = validation.validate_author(value)

    @property
    def year(self):
        return self._year
    @year.setter
    def year(self, value):
        self._year = validation.validate_year(value)

    @property
    def pages(self):
        return self._pages
    @pages.setter
    def pages(self, value):
        self._pages = validation.validate_pages(value)

    @property
    def is_loaned(self):
        return self._is_loaned

    def issue(self):
        if self._is_loaned:
            raise RuntimeError(f"Книга '{self._title}' уже выдана")
        self._is_loaned = True

    def return_book(self):
        if not self._is_loaned:
            raise RuntimeError(f"Книга '{self._title}' не была выдана")
        self._is_loaned = False

    # ----- Абстрактный метод для полиморфизма -----
    @abstractmethod
    def get_reading_time(self) -> int:
        """Вернуть предполагаемое время чтения в минутах."""
        pass

    # ----- Магические методы -----
    def __str__(self):
        status = "выдана" if self._is_loaned else "доступна"
        return f"«{self._title}» {self._author} ({self._year}) – {status}"

    def __repr__(self):
        return (f"Book(title='{self._title}', author='{self._author}', "
                f"year={self._year}, pages={self._pages}, is_loaned={self._is_loaned})")

    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return (self._title == other._title and
                self._author == other._author and
                self._year == other._year)