# -*- coding: utf-8 -*-
from model import Book

class Library:
    """Коллекция книг (библиотека). Реализует все методы для управления."""
    
    def __init__(self):
        self._items = []          # внутренний список книг
    
    # ---------- Базовые операции ----------
    def add(self, book: Book):
        """Добавить книгу с проверкой типа и дубликатов."""
        if not isinstance(book, Book):
            raise TypeError("Можно добавлять только объекты Book")
        # Проверка на дубликат (используем __eq__ из Book)
        for existing in self._items:
            if existing == book:
                raise ValueError(f"Книга '{book.title}' уже есть в библиотеке")
        self._items.append(book)
    
    def remove(self, book: Book):
        """Удалить книгу из коллекции."""
        self._items.remove(book)
    
    def get_all(self):
        """Вернуть копию списка всех книг."""
        return self._items.copy()
    
    # ---------- Поиск ----------
    def find_by_title(self, title: str):
        """Вернуть список книг, содержащих подстроку в названии."""
        title_lower = title.lower()
        return [b for b in self._items if title_lower in b.title.lower()]
    
    def find_by_author(self, author: str):
        """Вернуть список книг, содержащих подстроку в имени автора."""
        author_lower = author.lower()
        return [b for b in self._items if author_lower in b.author.lower()]
    
    def find_by_year(self, year: int):
        """Вернуть список книг с точным годом издания."""
        return [b for b in self._items if b.year == year]
    
    # ---------- Магические методы ----------
    def __len__(self):
        return len(self._items)
    
    def __iter__(self):
        return iter(self._items)
    
    def __getitem__(self, index):
        """Поддержка индексации: library[0], library[-1]."""
        return self._items[index]
    
    # ---------- Дополнительные методы ----------
    def remove_at(self, index: int):
        """Удалить книгу по индексу."""
        if 0 <= index < len(self._items):
            del self._items[index]
        else:
            raise IndexError("Индекс вне диапазона")
    
    def sort(self, key=None, reverse=False):
        """Сортировка книг по заданному ключу (например, lambda b: b.year)."""
        self._items.sort(key=key, reverse=reverse)
    
    # ---------- Логические операции (фильтрация) ----------
    def get_available(self):
        """Вернуть новую библиотеку только с доступными (не выданными) книгами."""
        new_lib = Library()
        for book in self._items:
            if not book.is_loaned:
                new_lib.add(book)
        return new_lib
    
    def get_loaned(self):
        """Вернуть новую библиотеку только с выданными книгами."""
        new_lib = Library()
        for book in self._items:
            if book.is_loaned:
                new_lib.add(book)
        return new_lib
    
    def filter_by_year(self, min_year: int, max_year: int):
        """Вернуть новую библиотеку с книгами в указанном диапазоне годов."""
        new_lib = Library()
        for book in self._items:
            if min_year <= book.year <= max_year:
                new_lib.add(book)
        return new_lib