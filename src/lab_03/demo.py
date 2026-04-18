from base import Book
from models import PrintedBook, Ebook, AudioBook
from collection import Library

print("=== Лабораторная работа №3: Наследование и иерархия классов ===\n")

# ----- Сценарий 1: создание объектов разных типов -----
printed = PrintedBook("Война и мир", "Лев Толстой", 1869, 1300, "твердая", True)
ebook = Ebook("Преступление и наказание", "Фёдор Достоевский", 1866, 400, 2.5, "epub")
audiobook = AudioBook("Мастер и Маргарита", "Михаил Булгаков", 1967, 480, 720, "Алексей Ковтун")

# ----- Сценарий 2: создание коллекции и добавление -----
lib = Library()
lib.add(printed)
lib.add(ebook)
lib.add(audiobook)

print("Содержимое библиотеки:")
for book in lib:
    print(f"  {book}")

# ----- Сценарий 3: полиморфный метод get_reading_time() -----
print("\n--- Время чтения (полиморфизм) ---")
for book in lib:
    print(f"{book.title}: {book.get_reading_time()} мин.")

# ----- Сценарий 4: проверка типов через isinstance -----
print("\n--- Проверка типов ---")
for book in lib:
    if isinstance(book, PrintedBook):
        print(f"{book.title} - печатная книга")
    elif isinstance(book, Ebook):
        print(f"{book.title} - электронная книга")
    elif isinstance(book, AudioBook):
        print(f"{book.title} - аудиокнига")

# ----- Сценарий 5: фильтрация коллекции по типу -----
print("\n--- Фильтрация по типу ---")
printed_lib = lib.get_printed_books()
print(f"Печатные книги ({len(printed_lib)}):")
for b in printed_lib:
    print(f"  {b}")

ebook_lib = lib.get_ebooks()
print(f"\nЭлектронные книги ({len(ebook_lib)}):")
for b in ebook_lib:
    print(f"  {b}")

audiobook_lib = lib.get_audiobooks()
print(f"\nАудиокниги ({len(audiobook_lib)}):")
for b in audiobook_lib:
    print(f"  {b}")

# ----- Сценарий 6: демонстрация работы методов базового класса (выдача) -----
print("\n--- Выдача книги (метод базового класса) ---")
printed.issue()
print(f"После выдачи: {printed}")
printed.return_book()
print(f"После возврата: {printed}")

# ----- Сценарий 7: сортировка коллекции (работает для любых наследников) -----
print("\n--- Сортировка по году ---")
lib.sort(key=lambda b: b.year)
for book in lib:
    print(f"  {book.year} – {book}")

print("\n=== Демонстрация завершена ===")

