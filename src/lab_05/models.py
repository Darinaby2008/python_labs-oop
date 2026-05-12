# -*- coding: utf-8 -*-
import validation

class Book:
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

class PrintedBook(Book):
    def __init__(self, title, author, year, pages, cover_type: str, is_illustrated: bool):
        super().__init__(title, author, year, pages)
        self.cover_type = cover_type
        self.is_illustrated = is_illustrated

    def __str__(self):
        base = super().__str__()
        illustr = ", иллюстрирована" if self.is_illustrated else ""
        return f"{base} [Печатная, обложка: {self.cover_type}{illustr}]"

class Ebook(Book):
    def __init__(self, title, author, year, pages, file_size: float, file_format: str):
        super().__init__(title, author, year, pages)
        self.file_size = file_size
        self.file_format = file_format

    def __str__(self):
        base = super().__str__()
        return f"{base} [Электронная, {self.file_format}, {self.file_size} МБ]"

class AudioBook(Book):
    def __init__(self, title, author, year, pages, duration: int, narrator: str):
        super().__init__(title, author, year, pages)
        self.duration = duration
        self.narrator = narrator

    def __str__(self):
        base = super().__str__()
        return f"{base} [Аудиокнига, {self.duration} мин, читает {self.narrator}]"