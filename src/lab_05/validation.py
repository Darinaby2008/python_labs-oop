"""Модуль с функциями валидации данных для класса Book."""

def validate_title(value):
    """Проверка корректности названия книги."""
    if not isinstance(value, str):
        raise TypeError("Название должно быть строкой")
    if not value.strip():
        raise ValueError("Название не может быть пустым")
    return value.strip()

def validate_author(value):
    """Проверка корректности имени автора."""
    if not isinstance(value, str):
        raise TypeError("Автор должен быть строкой")
    if not value.strip():
        raise ValueError("Автор не может быть пустым")
    return value.strip()

def validate_year(value):
    """Проверка корректности года издания."""
    if not isinstance(value, int):
        raise TypeError("Год должен быть целым числом")
    if value < 1600 or value > 2026:  # примерные границы
        raise ValueError("Год должен быть в диапазоне 1600–2026")
    return value

def validate_pages(value):
    """Проверка корректности количества страниц."""
    if not isinstance(value, int):
        raise TypeError("Количество страниц должно быть целым числом")
    if value <= 0:
        raise ValueError("Количество страниц должно быть положительным")
    return value