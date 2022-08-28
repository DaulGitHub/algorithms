from unittest import TestCase
from hw4datastructs.priorityqueue.queue import Priority, PriorityQueue, Item


class TestPriorityQueue(TestCase):

    def test_enqueue_set_to_middle(self):

        queue = PriorityQueue()
        value_1 = 7
        value_2 = 6
        value_3 = 4

        item_1 = Item(value_1)
        item_2 = Item(value_2)
        item_3 = Item(value_3)

        queue.enqueue(Priority.HI, item_1)
        queue.enqueue(Priority.LOW, item_2)
        queue.enqueue(Priority.MID, item_3)

        for i in range(3):
            item = queue.dequeue()
            if i == 0:
                self.assertEqual(value_1, item.value)
            elif i == 1:
                self.assertEqual(value_3, item.value)
            elif i == 2:
                self.assertEqual(value_2, item.value)

    def test_enqueue_set_to_end(self):

        queue = PriorityQueue()
        value_1 = 7
        value_2 = 6
        value_3 = 4

        item_1 = Item(value_1)
        item_2 = Item(value_2)
        item_3 = Item(value_3)

        queue.enqueue(Priority.MID, item_2)
        queue.enqueue(Priority.LOW, item_3)
        queue.enqueue(Priority.HI, item_1)

        for i in range(3):
            item = queue.dequeue()
            if i == 0:
                self.assertEqual(value_1, item.value)
            elif i == 1:
                self.assertEqual(value_2, item.value)
            elif i == 2:
                self.assertEqual(value_3, item.value)

    def test_enqueue_set_to_begin(self):

        queue = PriorityQueue()
        value_1 = 7
        value_2 = 6
        value_3 = 4

        item_1 = Item(value_1)
        item_2 = Item(value_2)
        item_3 = Item(value_3)

        queue.enqueue(Priority.HI, item_1)
        queue.enqueue(Priority.MID, item_2)
        queue.enqueue(Priority.LOW, item_3)

        for i in range(3):
            item = queue.dequeue()
            if i == 0:
                self.assertEqual(value_1, item.value)
            elif i == 1:
                self.assertEqual(value_2, item.value)
            elif i == 2:
                self.assertEqual(value_3, item.value)
