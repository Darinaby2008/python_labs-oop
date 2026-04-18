from models import PrintedBook, Ebook, AudioBook
from collection import Library
from interfaces import Printable, Comparable

# Универсальная функция, работающая через интерфейс Printable
def print_all(items):
    """Принимает итерируемую коллекцию объектов Printable и выводит их to_string()."""
    for item in items:
        print(item.to_string())

# Универсальная функция сортировки через интерфейс Comparable
def sort_by_comparable(items):
    """Сортирует список объектов, реализующих Comparable, используя compare_to."""
    # Простая пузырьковая сортировка для демонстрации
    n = len(items)
    for i in range(n):
        for j in range(0, n-i-1):
            if items[j].compare_to(items[j+1]) > 0:
                items[j], items[j+1] = items[j+1], items[j]
    return items

def main():
    print("=== Лабораторная работа №4: Интерфейсы и ABC ===\n")

    # ----- Создание объектов разных типов -----
    printed = PrintedBook("Война и мир", "Лев Толстой", 1869, 1300, "твердая", True)
    ebook = Ebook("Преступление и наказание", "Фёдор Достоевский", 1866, 400, 2.5, "epub")
    audiobook = AudioBook("Мастер и Маргарита", "Михаил Булгаков", 1967, 480, 720, "Алексей Ковтун")
    another_printed = PrintedBook("Анна Каренина", "Лев Толстой", 1877, 800, "мягкая", False)

    # ----- Коллекция -----
    lib = Library()
    lib.add(printed)
    lib.add(ebook)
    lib.add(audiobook)
    lib.add(another_printed)

    print("Содержимое библиотеки (через to_string()):")
    print_all(lib)   # универсальная функция через интерфейс Printable

    # ----- Проверка типов через isinstance -----
    print("\n--- Проверка isinstance ---")
    for book in lib:
        if isinstance(book, Printable):
            print(f"{book.title} реализует Printable")
        if isinstance(book, Comparable):
            print(f"{book.title} реализует Comparable")

    # ----- Демонстрация полиморфизма через интерфейс (сравнение) -----
    print("\n--- Сравнение книг через интерфейс Comparable ---")
    print(f"Сравнение '{printed.title}' и '{ebook.title}': {printed.compare_to(ebook)}")
    # Отрицательное число, т.к. 1869 - 1866 = 3 (positive, но ожидаем? На самом деле printed год больше, значит printed > ebook)
    # По нашей реализации compare_to возвращает разницу годов, что корректно.

    # ----- Сортировка через интерфейс Comparable (универсальная функция) -----
    print("\n--- Сортировка списка книг по году через Comparable ---")
    books_list = [printed, ebook, audiobook, another_printed]
    sorted_books = sort_by_comparable(books_list)
    for b in sorted_books:
        print(f"{b.year} – {b.title}")

    # ----- Фильтрация коллекции по интерфейсам -----
    print("\n--- Фильтрация библиотеки по интерфейсу Printable ---")
    printable_lib = lib.get_printable()
    print(f"Объектов, реализующих Printable: {len(printable_lib)}")
    for b in printable_lib:
        print(f"  {b.to_string()}")

    print("\n--- Фильтрация библиотеки по интерфейсу Comparable ---")
    comparable_lib = lib.get_comparable()
    print(f"Объектов, реализующих Comparable: {len(comparable_lib)}")
    for b in comparable_lib:
        print(f"  {b.to_string()}")

    # ----- Полиморфизм через интерфейс (без условий) -----
    print("\n--- Полиморфизм: вызов to_string() для разных объектов ---")
    # Создаём список объектов, не зная их конкретных типов
    random_objects = [printed, ebook, audiobook, another_printed]
    for obj in random_objects:
        print(obj.to_string())   # каждый объект сам знает, как представиться

    print("\n=== Демонстрация завершена ===")

if __name__ == "__main__":
    main()