from random import randrange


def bubble_sort(items: list) -> None:
    length = len(items)
    for i in range(length):
        for j in range(length-i-1):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]


if __name__ == "__main__":
    unsorted = [randrange(0, 10, 1) for i in range(10)]
    print(unsorted)
    bubble_sort(unsorted)
    print(unsorted)
