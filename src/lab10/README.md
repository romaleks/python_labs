## Лабораторная работа 10

## 1. Краткая теория

### Стек (Stack)
Стек — это структура данных типа *LIFO* (Last In — First Out).  
Последний добавленный элемент извлекается первым.

**Типичные операции:**
- `push(x)` — добавить элемент (O(1))
- `pop()` — удалить и вернуть верхний элемент (O(1))
- `peek()` — посмотреть верхний элемент без удаления (O(1))
- `len()` — количество элементов (O(1))

---

### Очередь (Queue)
Очередь — структура данных типа *FIFO* (First In — First Out).  
Первым извлекается элемент, добавленный раньше всех.

**Типичные операции:**
- `enqueue(x)` — добавить элемент (O(1))
- `dequeue()` — удалить и вернуть первый элемент (O(1))
- `peek()` — посмотреть первый элемент (O(1))
- `len()` — количество элементов (O(1))

---

### Односвязный список (Singly Linked List)
Список состоит из узлов `Node`, где каждый узел содержит:
- значение (`value`)
- ссылку на следующий узел (`next`)

Доступ по индексу — **медленный (O(n))**, так как нужно идти от головы.

**Типичные операции:**
- `append(x)` — добавить в конец (O(n) или O(1) при хвосте)
- `prepend(x)` — добавить в начало (O(1))
- `insert(i, x)` — вставить по индексу (O(n))
- `remove_at(i)` или `remove(value)` — удалить (O(n))
- `iter` — обход списка (O(n))
- `len()` — получить размер (O(1))

## 2. Выводы по бенчмаркам
### Самые быстрые структуры:
- Стек и очередь, реализованные на базе Python list или deque.
- Все операции выполняются за O(1) благодаря оптимизациям массива.

### Медленная структура:
- Односвязный список, потому что:
    - нет случайного доступа (вставка по индексу → O(n))
    - добавление в конец без tail требует полного прохода по списку
    - удаление по индексу тоже требует линейного обхода

### Итоги:
- Для частых вставок/удалений в конец → лучше стек/очередь.
- Для случайного доступа → связный список не подходит.
- Связный список выигрывает только если нужно дёшево вставлять в начало (O(1)).

### Задание A

```python
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
```

### Задание B 

```python
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, value):
        """Добавить элемент в конец списка"""
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self._size += 1
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node
        self._size += 1

    def prepend(self, value):
        """Добавить элемент в начало списка"""
        new_node = Node(value, next=self.head)
        self.head = new_node
        self._size += 1

    def insert(self, idx, value):
        """Вставка по индексу"""
        if idx < 0 or idx > self._size:
            raise IndexError("index out of range")

        if idx == 0:
            self.prepend(value)
            return

        new_node = Node(value)

        current = self.head
        for _ in range(idx - 1):
            current = current.next

        new_node.next = current.next
        current.next = new_node
        self._size += 1

    def remove_at(self, idx):
        """Удалить элемент по индексу"""
        if idx < 0 or idx >= self._size:
            raise IndexError("index out of range")

        if idx == 0:
            self.head = self.head.next
            self._size -= 1
            return

        current = self.head
        for _ in range(idx - 1):
            current = current.next

        current.next = current.next.next
        self._size -= 1

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def __len__(self):
        return self._size

    def __repr__(self):
        values = list(self)
        return f"SinglyLinkedList({values})"
```
