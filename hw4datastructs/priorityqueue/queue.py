# Приоритетная очередь (на выбор).
# Написать реализацию PriorityQueue - очередь с приоритетом.
# Варианты реализации - список списков, массив списков
# Методы к реализации:
# enqueue(int priority, T item) - поместить элемент в очередь
# T dequeue() - выбрать элемент из очереди

from enum import Enum, unique
from typing import TypeVar, Union


@unique
class Priority(Enum):

    HI = 6
    MID = 5
    LOW = 4


TItem = TypeVar("TItem", bound="Item")


class Item:

    def __init__(self, value: int):
        self.value = value
        self.priority = None
        self.previous = None

    def set_priority(self, priority: Priority):
        self.priority = priority


class PriorityQueue:

    def __init__(self):

        self._queue = None

    def enqueue(self, priority: Priority, item: TItem) -> None:

        item.priority = priority
        if self._queue is None:
            item.set_priority(priority)
            self._queue = item
        elif item.priority.value > self._queue.priority.value:
            item.previous = self._queue
            self._queue = item
        else:
            current_item = self._queue
            next_item = current_item
            while current_item is not None and item.priority.value <= current_item.priority.value:
                next_item = current_item
                current_item = current_item.previous

            item.previous = current_item
            next_item.previous = item

    def dequeue(self) -> Union[TItem, None]:

        item = self._queue
        if self._queue is not None:
            self._queue = self._queue.previous

        return item
