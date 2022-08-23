from unittest import TestCase
from hw4datastructs.dynamicarray.single_array import SingleArray


class TestSingleArray(TestCase):

    def test_add(self):

        arr = SingleArray()
        arr.add(4)
        arr.add(6)
        arr.add(9)

        self.assertEqual(arr.arr, [4, 6, 9])

    def test_get(self):

        arr = SingleArray()
        arr.add(4)
        arr.add(6)
        arr.add(9)

        self.assertEqual(arr.get(1), 6)

    def test_remove(self):

        arr = SingleArray()
        arr.add(4)
        arr.add(6)
        arr.add(9)

        self.assertEqual(arr.remove(1), 6)
        self.assertEqual(len(arr.arr), 2)

    def test_put(self):

        arr = SingleArray()
        arr.add(4)
        arr.add(6)
        arr.add(9)

        arr.put(8, 1)
        self.assertEqual(arr.arr, [4, 8, 6, 9])
