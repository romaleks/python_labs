from collections import deque
from typing import Any


class Stack:
    """Класс стек (LIFO) на основе list."""

    def __init__(self):
        self._data: list[Any] = []

    def push(self, item: Any) -> None:
        """Добавить элемент на вершину стека."""
        self._data.append(item)

    def pop(self) -> Any:
        """
        Снять и вернуть верхний элемент стека.
        Если стек пуст — бросить IndexError.
        """
        if not self._data:
            raise IndexError("pop from empty Stack")
        return self._data.pop()

    def peek(self) -> Any | None:
        """
        Вернуть верхний элемент без удаления.
        Если стек пуст — вернуть None.
        """
        if not self._data:
            return None
        return self._data[-1]

    def is_empty(self) -> bool:
        """Проверить, пуст ли стек."""
        return len(self._data) == 0

    def __len__(self) -> int:
        """Количество элементов в стеке."""
        return len(self._data)


class Queue:
    """Класс очередь (FIFO) на основе deque."""

    def __init__(self):
        self._data: deque[Any] = deque()

    def enqueue(self, item: Any) -> None:
        """Добавить элемент в конец очереди."""
        self._data.append(item)

    def dequeue(self) -> Any:
        """
        Удалить и вернуть первый элемент очереди.
        Если очередь пуста — бросить IndexError.
        """
        if not self._data:
            raise IndexError("dequeue from empty Queue")
        return self._data.popleft()

    def peek(self) -> Any | None:
        """
        Вернуть первый элемент без удаления.
        Если очередь пустая — вернуть None.
        """
        if not self._data:
            return None
        return self._data[0]

    def is_empty(self) -> bool:
        """Проверить, пустая ли очередь."""
        return len(self._data) == 0

    def __len__(self) -> int:
        """Количество элементов в очереди."""
        return len(self._data)
