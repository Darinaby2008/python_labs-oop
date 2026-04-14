from base import Book
from models import PrintedBook, Ebook, AudioBook

class Library:
    """Коллекция книг с поддержкой полиморфизма."""
    def __init__(self):
        self._items = []

    def add(self, book: Book):
        if not isinstance(book, Book):
            raise TypeError("Можно добавлять только объекты Book или его наследников")
        # Проверка дубликатов (использует __eq__ из Book)
        if any(b == book for b in self._items):
            raise ValueError(f"Книга '{book.title}' уже есть в библиотеке")
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

    # ----- Поиск (без изменений) -----
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

    # ----- Сортировка -----
    def sort(self, key=None, reverse=False):
        self._items.sort(key=key, reverse=reverse)

    # ----- Логические операции (фильтрация по статусу) -----
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

    # ----- НОВОЕ: фильтрация по типу (для задания 5) -----
    def get_printed_books(self):
        """Вернуть новую библиотеку, содержащую только PrintedBook."""
        new_lib = Library()
        for b in self._items:
            if isinstance(b, PrintedBook):
                new_lib.add(b)
        return new_lib

    def get_ebooks(self):
        new_lib = Library()
        for b in self._items:
            if isinstance(b, Ebook):
                new_lib.add(b)
        return new_lib

    def get_audiobooks(self):
        new_lib = Library()
        for b in self._items:
            if isinstance(b, AudioBook):
                new_lib.add(b)
        return new_lib