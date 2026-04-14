from base import Book

class PrintedBook(Book):
    """Печатная книга."""
    def __init__(self, title, author, year, pages, cover_type: str, is_illustrated: bool):
        super().__init__(title, author, year, pages)
        self.cover_type = cover_type          # "твердая" или "мягкая"
        self.is_illustrated = is_illustrated

    def get_reading_time(self) -> int:
        """Время чтения: 2 минуты на страницу."""
        return self.pages * 2

    def __str__(self):
        base_str = super().__str__()
        illustr = ", иллюстрирована" if self.is_illustrated else ""
        return f"{base_str} [Печатная, обложка: {self.cover_type}{illustr}]"

    def __repr__(self):
        return (f"PrintedBook(title='{self.title}', author='{self.author}', "
                f"year={self.year}, pages={self.pages}, cover_type='{self.cover_type}', "
                f"is_illustrated={self.is_illustrated})")

class Ebook(Book):
    """Электронная книга."""
    def __init__(self, title, author, year, pages, file_size: float, file_format: str):
        super().__init__(title, author, year, pages)
        self.file_size = file_size      # МБ
        self.file_format = file_format  # pdf, epub, mobi

    def get_reading_time(self) -> int:
        """Время чтения: 1.5 минуты на страницу (быстрее из-за удобства)."""
        return int(self.pages * 1.5)

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str} [Электронная, {self.file_format}, {self.file_size} МБ]"

    def __repr__(self):
        return (f"Ebook(title='{self.title}', author='{self.author}', "
                f"year={self.year}, pages={self.pages}, file_size={self.file_size}, "
                f"file_format='{self.file_format}')")

class AudioBook(Book):
    """Аудиокнига."""
    def __init__(self, title, author, year, pages, duration: int, narrator: str):
        super().__init__(title, author, year, pages)
        self.duration = duration        # длительность в минутах
        self.narrator = narrator        # чтец

    def get_reading_time(self) -> int:
        """Время прослушивания – просто длительность аудиокниги."""
        return self.duration

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str} [Аудиокнига, {self.duration} мин, читает {self.narrator}]"

    def __repr__(self):
        return (f"AudioBook(title='{self.title}', author='{self.author}', "
                f"year={self.year}, pages={self.pages}, duration={self.duration}, "
                f"narrator='{self.narrator}')")