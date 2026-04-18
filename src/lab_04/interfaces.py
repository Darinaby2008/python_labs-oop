from abc import ABC, abstractmethod

class Printable(ABC):
    """Интерфейс для объектов, которые могут быть представлены в виде строки."""
    @abstractmethod
    def to_string(self) -> str:
        """Вернуть строковое представление объекта (для отображения)."""
        pass

class Comparable(ABC):
    """Интерфейс для объектов, которые можно сравнивать."""
    @abstractmethod
    def compare_to(self, other) -> int:
        """
        Сравнить текущий объект с other.
        Возвращает:
            отрицательное число, если self < other
            0, если self == other
            положительное число, если self > other
        """
        pass
    