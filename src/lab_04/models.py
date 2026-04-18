from abc import ABC
from interfaces import Printable, Comparable
import validation   # из ЛР-1 (скопировать в папку lab04)

class Book(Printable, Comparable):
    """Базовый класс книги, реализует интерфейсы Printable и Comparable."""
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

    # ----- Реализация интерфейса Printable -----
    def to_string(self) -> str:
        """Строковое представление для интерфейса Printable."""
        status = "выдана" if self._is_loaned else "доступна"
        return f"«{self._title}» {self._author} ({self._year}) – {status}"

    # ----- Реализация интерфейса Comparable (сравнение по году) -----
    def compare_to(self, other) -> int:
        if not isinstance(other, Book):
            raise TypeError("Можно сравнивать только с объектами Book")
        return self._year - other._year

    # ----- Магические методы (для удобства) -----
    def __str__(self):
        return self.to_string()

    def __repr__(self):
        return (f"Book(title='{self._title}', author='{self._author}', "
                f"year={self._year}, pages={self._pages}, is_loaned={self._is_loaned})")

    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return (self._title == other._title and
                self._author == other._author and
                self._year == other._year)


# ----- Дочерние классы (наследуют реализацию интерфейсов) -----
class PrintedBook(Book):
    def __init__(self, title, author, year, pages, cover_type: str, is_illustrated: bool):
        super().__init__(title, author, year, pages)
        self.cover_type = cover_type
        self.is_illustrated = is_illustrated

    def to_string(self) -> str:
        # Переопределяем для добавления деталей
        base = super().to_string()
        illustr = ", иллюстрирована" if self.is_illustrated else ""
        return f"{base} [Печатная, обложка: {self.cover_type}{illustr}]"

    def __repr__(self):
        return (f"PrintedBook(title='{self.title}', author='{self.author}', "
                f"year={self.year}, pages={self.pages}, cover_type='{self.cover_type}', "
                f"is_illustrated={self.is_illustrated})")


class Ebook(Book):
    def __init__(self, title, author, year, pages, file_size: float, file_format: str):
        super().__init__(title, author, year, pages)
        self.file_size = file_size
        self.file_format = file_format

    def to_string(self) -> str:
        base = super().to_string()
        return f"{base} [Электронная, {self.file_format}, {self.file_size} МБ]"

    def __repr__(self):
        return (f"Ebook(title='{self.title}', author='{self.author}', "
                f"year={self.year}, pages={self.pages}, file_size={self.file_size}, "
                f"file_format='{self.file_format}')")


class AudioBook(Book):
    def __init__(self, title, author, year, pages, duration: int, narrator: str):
        super().__init__(title, author, year, pages)
        self.duration = duration
        self.narrator = narrator

    def to_string(self) -> str:
        base = super().to_string()
        return f"{base} [Аудиокнига, {self.duration} мин, читает {self.narrator}]"

    # Сравнение аудиокниг можно переопределить, но оставим как у Book (по году)

    def __repr__(self):
        return (f"AudioBook(title='{self.title}', author='{self.author}', "
                f"year={self.year}, pages={self.pages}, duration={self.duration}, "
                f"narrator='{self.narrator}')")