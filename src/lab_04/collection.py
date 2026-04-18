from interfaces import Printable, Comparable
from models import Book

class Library:
    def __init__(self):
        self._items = []

    def add(self, book: Book):
        if not isinstance(book, Book):
            raise TypeError("Можно добавлять только объекты Book")
        if any(b == book for b in self._items):
            raise ValueError(f"Книга '{book.title}' уже есть")
        self._items.append(book)

    def remove(self, book: Book):
        self._items.remove(book)

    def remove_at(self, index: int):
        if 0 <= index < len(self._items):
            del self._items[index]
        else:
            raise IndexError("Индекс вне диапазона")

    def get_all(self):
        return self._items.copy()

    # ----- Поиск -----
    def find_by_title(self, title):
        title_lower = title.lower()
        return [b for b in self._items if title_lower in b.title.lower()]

    def find_by_author(self, author):
        author_lower = author.lower()
        return [b for b in self._items if author_lower in b.author.lower()]

    # ----- Магические методы -----
    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def sort(self, key=None, reverse=False):
        self._items.sort(key=key, reverse=reverse)

    # ----- Фильтрация по статусу -----
    def get_available(self):
        new_lib = Library()
        for b in self._items:
            if not b.is_loaned:
                new_lib.add(b)
        return new_lib

    def get_loaned(self):
        new_lib = Library()
        for b in self._items:
            if b.is_loaned:
                new_lib.add(b)
        return new_lib

    # ----- НОВОЕ: фильтрация по интерфейсам (задание 5) -----
    def get_printable(self):
        """Вернуть новую библиотеку, содержащую только объекты, реализующие Printable."""
        new_lib = Library()
        for b in self._items:
            if isinstance(b, Printable):
                new_lib.add(b)
        return new_lib

    def get_comparable(self):
        """Вернуть новую библиотеку, содержащую только объекты, реализующие Comparable."""
        new_lib = Library()
        for b in self._items:
            if isinstance(b, Comparable):
                new_lib.add(b)
        return new_lib