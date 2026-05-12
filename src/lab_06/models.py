class Book:
    total_books = 0

    def __init__(self, title: str, author: str, year: int, pages: int) -> None:
        self._title: str = title
        self._author: str = author
        self._year: int = year
        self._pages: int = pages
        self._is_loaned: bool = False
        Book.total_books += 1

    @property
    def title(self) -> str: return self._title
    @property
    def author(self) -> str: return self._author
    @property
    def year(self) -> int: return self._year
    @property
    def pages(self) -> int: return self._pages
    @property
    def is_loaned(self) -> bool: return self._is_loaned

    # Методы для протоколов (достаточно наличия, наследования нет)
    def display(self) -> str:
        status = "выдана" if self._is_loaned else "доступна"
        return f"«{self._title}» {self._author} ({self._year}) – {status}"

    def score(self) -> float:
        # Простой рейтинг: базовые 100 баллов минус возраст, плюс бонус за страницы
        age_penalty = (2025 - self._year) * 0.5
        pages_bonus = self._pages / 1000.0 * 10
        return max(0.0, 100.0 - age_penalty + pages_bonus)

class PrintedBook(Book):
    def __init__(self, title: str, author: str, year: int, pages: int,
                 cover_type: str, is_illustrated: bool) -> None:
        super().__init__(title, author, year, pages)
        self.cover_type: str = cover_type
        self.is_illustrated: bool = is_illustrated

    def display(self) -> str:
        base = super().display()
        illustr = ", иллюстрирована" if self.is_illustrated else ""
        return f"{base} [Печатная, обложка: {self.cover_type}{illustr}]"

class Ebook(Book):
    def __init__(self, title: str, author: str, year: int, pages: int,
                 file_size: float, file_format: str) -> None:
        super().__init__(title, author, year, pages)
        self.file_size: float = file_size
        self.file_format: str = file_format

    def display(self) -> str:
        base = super().display()
        return f"{base} [Электронная, {self.file_format}, {self.file_size} МБ]"

class AudioBook(Book):
    def __init__(self, title: str, author: str, year: int, pages: int,
                 duration: int, narrator: str) -> None:
        super().__init__(title, author, year, pages)
        self.duration: int = duration
        self.narrator: str = narrator

    def display(self) -> str:
        base = super().display()
        return f"{base} [Аудиокнига, {self.duration} мин, читает {self.narrator}]"