from models import PrintedBook, Ebook, AudioBook, Book   
from container import TypedCollection, Displayable, Scorable, D, S


print("=== Лабораторная работа №6: Generics, typing, Protocol ===\n")

# ----- Сценарий 1: TypedCollection[D] с объектами разных типов (Displayable) -----
print("--- Сценарий 1: Коллекция Displayable (разные типы книг) ---")
display_collection = TypedCollection[D]()   # ограничение: у объектов должен быть display()
pb = PrintedBook("Война и мир", "Толстой", 1869, 1300, "твердая", True)
ab = AudioBook("Мастер и Маргарита", "Булгаков", 1967, 480, 720, "Ковтун")
eb = Ebook("Преступление и наказание", "Достоевский", 1866, 400, 2.5, "epub")

display_collection.add(pb)
display_collection.add(ab)
display_collection.add(eb)

print("Все книги в Displayable-коллекции:")
for book in display_collection.get_all():
    print(f"  {book.display()}")   # вызов метода протокола

# ----- Сценарий 2: TypedCollection[S] (Scorable) -----
print("\n--- Сценарий 2: Коллекция Scorable (рейтинг книг) ---")
score_collection = TypedCollection[S]()
pb2 = PrintedBook("Анна Каренина", "Толстой", 1877, 800, "мягкая", False)
eb2 = Ebook("Идиот", "Достоевский", 1869, 600, 3.1, "pdf")
score_collection.add(pb2)
score_collection.add(eb2)

print("Книги и их рейтинги (score):")
for book in score_collection.get_all():
    print(f"  {book.display()} -> рейтинг: {book.score():.2f}")

# ----- Сценарий 3: find, filter, map (и демонстрация смены типа результата) -----
print("\n--- Сценарий 3: find, filter, map (на обычной коллекции) ---")
mixed = TypedCollection[Book]()
mixed.add(pb)
mixed.add(ab)
mixed.add(eb)
mixed.add(pb2)
mixed.add(eb2)

# find
found = mixed.find(lambda b: b.title == "Мастер и Маргарита")
print(f"find('Мастер и Маргарита'): {found.display() if found else 'None'}")
not_found = mixed.find(lambda b: b.title == "Неизвестная книга")
print(f"find('Неизвестная книга'): {not_found}")

# filter
modern = mixed.filter(lambda b: b.year > 1900)
print(f"\nfilter (год > 1900): {len(modern)} книг(и)")
for b in modern:
    print(f"  {b.display()}")

# map – демонстрация изменения типа результата
titles = mixed.map(lambda b: b.title)          # list[str]
years = mixed.map(lambda b: b.year)            # list[int]
scores = mixed.map(lambda b: b.score())        # list[float]
print("\nmap -> названия (list[str]):", titles)
print("map -> годы (list[int]):", years)
print("map -> рейтинги (list[float]):", [round(s,2) for s in scores])

# Проверка, что объекты не наследуют протоколы, но подходят
print("\n--- Проверка: объекты не наследуют протоколы, но подходят ---")
print(f"PrintedBook — наследник Displayable? (isinstance): {isinstance(pb, Displayable)}")
print(f"PrintedBook — наследник Scorable? (isinstance): {isinstance(pb, Scorable)}")
print("Тем не менее, оба объекта были добавлены в коллекции с ограничениями,")
print("потому что протоколы проверяют наличие методов, а не наследование.")

print("\n=== Демонстрация завершена ===")

