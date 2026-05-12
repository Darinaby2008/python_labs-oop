#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Лабораторная работа №5: Функции как аргументы. Стратегии и делегаты.
Демонстрация всех возможностей на коллекции книг.
"""
from models import PrintedBook, Ebook, AudioBook
from collection import Library
from strategies import (
    by_title, by_year, by_pages, by_year_then_title,
    is_available, is_printed, is_ebook,
    make_year_filter, to_short_string, add_star_to_title,
    DiscountStrategy, AddPrefixStrategy
)

def print_library(lib, title="Коллекция"):
    """Вспомогательная функция для вывода коллекции."""
    print(f"\n{title} (всего книг: {len(lib)}):")
    for book in lib:
        print(f"  {book}")

def main():
        print("=== Лабораторная работа №5: Функции как аргументы ===")

        # ----- Создание коллекции из 5+ книг разных типов -----
        lib = Library()
        lib.add(PrintedBook("Война и мир", "Лев Толстой", 1869, 1300, "твердая", True))
        lib.add(Ebook("Преступление и наказание", "Фёдор Достоевский", 1866, 400, 2.5, "epub"))
        lib.add(AudioBook("Мастер и Маргарита", "Михаил Булгаков", 1967, 480, 720, "Алексей Ковтун"))
        lib.add(PrintedBook("Анна Каренина", "Лев Толстой", 1877, 800, "мягкая", False))
        lib.add(Ebook("Идиот", "Фёдор Достоевский", 1869, 600, 3.2, "pdf"))
        lib.add(PrintedBook("Тихий Дон", "Михаил Шолохов", 1940, 1500, "твердая", False))

        print_library(lib, "Исходная коллекция")

        # ==================== СЦЕНАРИЙ 1 ====================
        print("\n" + "="*60)
        print("СЦЕНАРИЙ 1: Цепочка операций filter → sort → apply")
        print("="*60)

        # 1. Фильтрация: только доступные (не выданные) книги
        available_lib = lib.filter_by(is_available)
        print_library(available_lib, "После фильтрации (только доступные)")

        # 2. Сортировка: по году издания (от старых к новым)
        available_lib.sort_by(by_year)
        print_library(available_lib, "После сортировки по году")

        # 3. Применение стратегии: добавить звёздочку к названию каждой книги
        available_lib.apply(add_star_to_title)
        print_library(available_lib, "После apply (добавлена ★ к названию)")

        # ==================== СЦЕНАРИЙ 2 ====================
        print("\n" + "="*60)
        print("СЦЕНАРИЙ 2: Замена стратегии без изменения кода коллекции")
        print("="*60)

        # Создаём копию исходной коллекции (через новый объект и добавление)
        lib2 = Library()
        for book in lib.get_all():
            lib2.add(book)

        print_library(lib2, "Исходная коллекция (копия)")

        # Сортировка по разным ключам
        print("\n--- Сортировка по названию (by_title) ---")
        lib2.sort_by(by_title)
        for book in lib2:
            print(f"  {book}")

        print("\n--- Сортировка по страницам (by_pages) ---")
        lib2.sort_by(by_pages)
        for book in lib2:
            print(f"  {book}")

        print("\n--- Сортировка по году, затем по названию (by_year_then_title) ---")
        lib2.sort_by(by_year_then_title)
        for book in lib2:
            print(f"  {book}")

        # Фильтрация разными предикатами
        print("\n--- Фильтрация: только электронные книги ---")
        ebooks = lib2.filter_by(is_ebook)
        for book in ebooks:
            print(f"  {book}")

        print("\n--- Фильтрация: только печатные книги ---")
        printed_books = lib2.filter_by(is_printed)
        for book in printed_books:
            print(f"  {book}")

        # Фильтр, созданный фабрикой (годы 1860-1880)
        print("\n--- Фильтрация по диапазону годов (1860-1880) через фабрику ---")
        year_filter = make_year_filter(1860, 1880)
        filtered_by_year = lib2.filter_by(year_filter)
        for book in filtered_by_year:
            print(f"  {book}")

        # ==================== СЦЕНАРИЙ 3 ====================
        print("\n" + "="*60)
        print("СЦЕНАРИЙ 3: Callable-объект как стратегия (паттерн Стратегия)")
        print("="*60)

        lib3 = Library()
        lib3.add(PrintedBook("Книга 1", "Автор A", 2000, 300, "мягкая", False))
        lib3.add(Ebook("Книга 2", "Автор B", 2001, 250, 1.2, "epub"))
        lib3.add(PrintedBook("Книга 3", "Автор C", 2002, 400, "твердая", True))

        print_library(lib3, "Исходная коллекция для callable-стратегий")

        # Применяем стратегию DiscountStrategy (уменьшаем количество страниц на 20%)
        discount_strategy = DiscountStrategy(20)
        lib3.apply(discount_strategy)
        print_library(lib3, "После применения DiscountStrategy (страницы уменьшены на 20%)")

        # Применяем стратегию AddPrefixStrategy (добавляем префикс "[NEW] ")
        prefix_strategy = AddPrefixStrategy("[NEW] ")
        lib3.apply(prefix_strategy)
        print_library(lib3, "После применения AddPrefixStrategy (добавлен префикс [NEW])")

        # Дополнительно: демонстрация map (преобразование коллекции в список строк)
        print("\n--- Применение map через метод map_to (to_short_string) ---")
        short_strings = lib3.map_to(to_short_string)
        for s in short_strings:
            print(f"  {s}")

        print("\n=== Демонстрация завершена ===")

if __name__ == "__main__":
    main()