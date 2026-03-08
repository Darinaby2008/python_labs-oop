"""Демонстрация работы класса Book."""

from model import Book

def main():
    print("Демонстрация работы класса Book\n" + "=" * 40)

    # ----- Сценарий 1: нормальное создание и вывод -----
    print("\n1. Создание объектов и вывод")
    book1 = Book("Война и мир", "Лев Толстой", 1869, 1300)
    book2 = Book("Преступление и наказание", "Фёдор Достоевский", 1866, 400)

    print("book1 (через __str__):", book1)
    print("book2 (через __str__):", book2)
    print("book1 (через __repr__):", repr(book1))
    print("book2 (через __repr__):", repr(book2))

    # ----- Сценарий 2: доступ к атрибуту класса -----
    print("\n2. Атрибут класса total_books")
    print(f"Через класс Book.total_books = {Book.total_books}")
    print(f"Через экземпляр book1.total_books = {book1.total_books}")

    # ----- Сценарий 3: сравнение книг -----
    print("\n3. Сравнение книг (__eq__)")
    book3 = Book("Война и мир", "Лев Толстой", 1869, 1300)  # те же данные
    print(f"book1 == book2? {book1 == book2}")
    print(f"book1 == book3? {book1 == book3}")  # должны быть равны

    # ----- Сценарий 4: изменение состояния (выдача/возврат) -----
    print("\n4. Изменение состояния (логика выдачи)")
    print("Исходное состояние book1:", book1)
    book1.issue()
    print("После выдачи (issue):", book1)
    try:
        book1.issue()  # повторная выдача
    except RuntimeError as e:
        print("Ошибка при повторной выдаче:", e)

    book1.return_book()
    print("После возврата (return_book):", book1)

    try:
        book1.return_book()  # возврат ещё раз
    except RuntimeError as e:
        print("Ошибка при повторном возврате:", e)

    # ----- Сценарий 5: изменение свойств через setter -----
    print("\n5. Изменение года и количества страниц (сеттеры с валидацией)")
    print("Текущий год book2:", book2.year)
    book2.year = 1867  # корректное значение
    print("Новый год book2:", book2.year)

    try:
        book2.year = 3000  # некорректный год
    except ValueError as e:
        print("Ошибка при установке года 3000:", e)

    print("Текущее количество страниц book2:", book2.pages)
    book2.pages = 450
    print("Новое количество страниц:", book2.pages)

    try:
        book2.pages = -100
    except ValueError as e:
        print("Ошибка при установке страниц -100:", e)

    # ----- Сценарий 6: некорректное создание (try/except) -----
    print("\n6. Попытки некорректного создания объектов")
    cases = [
        ("", "Пушкин", 1830, 100),           # пустое название
        ("Евгений Онегин", "", 1830, 200),   # пустой автор
        ("Руслан и Людмила", "Пушкин", 1300, 150),  # год слишком мал
        ("Пиковая дама", "Пушкин", 1834, -50)       # отрицательные страницы
    ]
    for i, (title, author, year, pages) in enumerate(cases, 1):
        try:
            b = Book(title, author, year, pages)
            print(f"Случай {i}: объект создан (не должно было случиться)")
        except (TypeError, ValueError) as e:
            print(f"Случай {i}: ошибка — {e}")

    # Итог
    print("\n" + "=" * 40)
    print("Демонстрация завершена.")

if __name__ == "__main__":
    main()