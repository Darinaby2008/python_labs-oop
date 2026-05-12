# -*- coding: utf-8 -*-
from models import Book

class Library:
    """Коллекция книг с поддержкой функциональных операций."""
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

    def get_all(self):
        return self._items.copy()

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        return self._items[index]

    # ----- Новые методы для работы со стратегиями -----
    def sort_by(self, key_func, reverse=False):
        """
        Сортирует текущую коллекцию по ключу, возвращает self (для цепочек).
        key_func - функция, принимающая книгу и возвращающая значение для сравнения.
        """
        self._items.sort(key=key_func, reverse=reverse)
        return self

    def filter_by(self, predicate):
        """
        Возвращает новую коллекцию, содержащую только элементы,
        удовлетворяющие условию predicate (функция, возвращающая bool).
        Исходная коллекция не изменяется.
        """
        new_lib = Library()
        for book in self._items:
            if predicate(book):
                new_lib.add(book)
        return new_lib

    def apply(self, func):
        """
        Применяет функцию func к каждому элементу коллекции (изменяет объекты).
        Возвращает self для цепочек.
        """
        for book in self._items:
            func(book)
        return self

    def map_to(self, func):
        """
        Применяет функцию func к каждому элементу и возвращает список результатов.
        Не изменяет коллекцию.
        """
        return [func(book) for book in self._items]