# -*- coding: utf-8 -*-
"""
Модуль содержит функции-стратегии для сортировки, фильтрации, преобразования,
а также фабрики функций и callable-объекты для паттерна Стратегия.
"""

# ---------- Стратегии сортировки (key-функции) ----------
def by_title(book):
    """Сортировка по названию (алфавит)."""
    return book.title

def by_author(book):
    """Сортировка по автору."""
    return book.author

def by_year(book):
    """Сортировка по году издания (от старых к новым)."""
    return book.year

def by_pages(book):
    """Сортировка по количеству страниц."""
    return book.pages

def by_year_then_title(book):
    """Сортировка сначала по году, затем по названию."""
    return (book.year, book.title)

# ---------- Функции-фильтры (предикаты) ----------
def is_available(book):
    """Фильтр: доступные книги (не выданы)."""
    return not book.is_loaned

def is_printed(book):
    """Фильтр: только печатные книги."""
    from models import PrintedBook
    return isinstance(book, PrintedBook)

def is_ebook(book):
    """Фильтр: только электронные книги."""
    from models import Ebook
    return isinstance(book, Ebook)

def is_audiobook(book):
    """Фильтр: только аудиокниги."""
    from models import AudioBook
    return isinstance(book, AudioBook)

# ---------- Фабрика функций (замыкание) ----------
def make_year_filter(min_year, max_year):
    """
    Возвращает функцию-предикат, которая проверяет, входит ли год книги в диапазон.
    Пример: filter_by_year = make_year_filter(1850, 1900)
    """
    def year_predicate(book):
        return min_year <= book.year <= max_year
    return year_predicate

# ---------- Функции для map (преобразование) ----------
def to_short_string(book):
    """Преобразует книгу в короткую строку: 'Название (Год)'."""
    return f"{book.title} ({book.year})"

def to_title_author(book):
    """Преобразует книгу в строку 'Автор: Название'."""
    return f"{book.author}: {book.title}"

# ---------- Функции для apply (изменение состояния) ----------
def add_star_to_title(book):
    """Добавляет звёздочку в начало названия (демонстрация apply)."""
    book.title = "★ " + book.title

def mark_as_rare(book):
    """Помечает книгу как редкую (добавляет метку в название)."""
    if "[Rare]" not in book.title:
        book.title = "[Rare] " + book.title

# ---------- Паттерн Стратегия через callable-объект ----------
class DiscountStrategy:
    """
    Callable-объект для применения скидки (гипотетической, например, уменьшение страниц).
    В реальном применении можно было бы изменять цену, но у книг её нет.
    Здесь для демонстрации уменьшаем количество страниц на 10%.
    """
    def __init__(self, percent):
        self.percent = percent

    def __call__(self, book):
        # Уменьшаем количество страниц на заданный процент (не может стать меньше 1)
        new_pages = int(book.pages * (1 - self.percent / 100))
        book.pages = max(1, new_pages)

class AddPrefixStrategy:
    """Callable-объект для добавления префикса к названию книги."""
    def __init__(self, prefix):
        self.prefix = prefix

    def __call__(self, book):
        if not book.title.startswith(self.prefix):
            book.title = self.prefix + book.title