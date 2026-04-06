from model import Book
from collection import Library


print("=== Лабораторная работа №2: Коллекция книг (Library) ===\n")
    
# ----- Создание книг -----
book1 = Book("Война и мир", "Лев Толстой", 1869, 1300)
book2 = Book("Преступление и наказание", "Фёдор Достоевский", 1866, 400)
book3 = Book("Анна Каренина", "Лев Толстой", 1877, 800)
book4 = Book("Мастер и Маргарита", "Михаил Булгаков", 1967, 480)
    
# ----- Создание библиотеки -----
lib = Library()
    
# Сценарий 1: добавление и итерация
print("Сценарий 1: Добавление книг")
lib.add(book1)
lib.add(book2)
lib.add(book3)
lib.add(book4)
print(f"В библиотеке {len(lib)} книг:")
for book in lib:
    print(f"  {book}")
    
# Проверка дубликата
print("\nПопытка добавить дубликат 'Война и мир':")
try:
    lib.add(Book("Война и мир", "Лев Толстой", 1869, 1300))
except ValueError as e:
    print(f"  Ошибка: {e}")
    
# Сценарий 2: поиск
print("\nСценарий 2: Поиск книг по автору 'Толстой'")
for book in lib.find_by_author("Толстой"):
    print(f"  {book}")
    
print("Поиск по названию, содержащему 'Маргарита':")
for book in lib.find_by_title("Маргарита"):
    print(f"  {book}")
    
# Сценарий 3: индексация и удаление по индексу
print("\nСценарий 3: Доступ по индексу")
print(f"Первая книга: {lib[0]}")
print(f"Последняя книга: {lib[-1]}")
lib.remove_at(2)   # удаляем "Анна Каренина"
print(f"После удаления книги с индексом 2 осталось {len(lib)} книг:")
for book in lib:
    print(f"  {book}")
    
# Сценарий 4: сортировка по году
print("\nСценарий 4: Сортировка по году (от старых к новым)")
lib.sort(key=lambda b: b.year)
for book in lib:
    print(f"  {book.year} – {book}")
    
# Сценарий 5: логические операции (выдача/доступность)
print("\nСценарий 5: Выдача книги и фильтрация по статусу")
book2.issue()   # выдаём "Преступление и наказание"
print(f"Книга '{book2.title}' выдана")
    
available = lib.get_available()
loaned = lib.get_loaned()
print(f"Доступные книги ({len(available)}):")
for book in available:
    print(f"  {book}")
print(f"Выданные книги ({len(loaned)}):")
for book in loaned:
    print(f"  {book}")
    
# Фильтрация по году
print("\nФильтрация по году (1860–1880):")
for book in lib.filter_by_year(1860, 1880):
    print(f"  {book}")
    
# Сценарий 6: удаление по объекту
print("\nСценарий 6: Удаление книги 'Война и мир'")
lib.remove(book1)
print(f"Осталось книг: {len(lib)}")
for book in lib:
    print(f"  {book}")
    
print("\n=== Демонстрация завершена ===")

