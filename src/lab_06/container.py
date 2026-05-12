from typing import TypeVar, Generic, Callable, Optional, List, Protocol, runtime_checkable

# ----- Протоколы (структурные интерфейсы) -----
@runtime_checkable
class Displayable(Protocol):
    def display(self) -> str:
        ...

@runtime_checkable
class Scorable(Protocol):
    def score(self) -> float:
        ...

# ----- TypeVar с ограничениями -----
D = TypeVar('D', bound=Displayable)
S = TypeVar('S', bound=Scorable)
T = TypeVar('T')
R = TypeVar('R')

# ----- Обобщённая коллекция -----
class TypedCollection(Generic[T]):
    def __init__(self) -> None:
        self._items: List[T] = []

    def add(self, item: T) -> None:
        self._items.append(item)

    def remove(self, item: T) -> None:
        self._items.remove(item)

    def get_all(self) -> List[T]:
        return list(self._items)

    def find(self, predicate: Callable[[T], bool]) -> Optional[T]:
        for item in self._items:
            if predicate(item):
                return item
        return None

    def filter(self, predicate: Callable[[T], bool]) -> List[T]:
        return [item for item in self._items if predicate(item)]

    def map(self, transform: Callable[[T], R]) -> List[R]:
        return [transform(item) for item in self._items]

    def __len__(self) -> int:
        return len(self._items)