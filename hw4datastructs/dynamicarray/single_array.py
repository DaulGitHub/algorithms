from hw4datastructs.dynamicarray.i_array import IArray


class SingleArray(IArray):
    """
    Implementation of a dynamic array.
    Increasing the size of the array by one element.
    """

    def __init__(self):
        self._length = 0
        self._capacity = 1
        self.arr = [None] * self._capacity

    def get(self, index: int) -> int:
        return self.arr[index]

    def remove(self, index: int) -> int:
        item = self.arr.pop(index)
        if self._length >= 0:
            self._length -= 1
        if self._capacity >= 0:
            self._capacity -= 1

        return item

    def add(self, item: int) -> None:
        if self._length < self._capacity:
            self.arr[self._length] = item
        else:
            self.arr = self._resize(self.arr)
            self.arr[self._length] = item

        self._length += 1

    def put(self, item: int, index: int = None) -> None:
        if index < 0:
            raise ValueError("index must be >= 0. index is {}".format(index))

        if self._length >= self._capacity-1:
            self.arr = self._resize(self.arr)

        for i in range(self._length, index-1, -1):
            self.arr[i] = self.arr[i-1]

        self._length += 1
        self.arr[index] = item

    def _resize(self, arr) -> list:
        self._capacity += 1
        resized_arr = [None] * self._capacity
        for i, item in enumerate(arr):
            resized_arr[i] = item

        return resized_arr

