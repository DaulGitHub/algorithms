
def count_bit1(digit: int) -> int:
    count = 0
    while digit > 0:
        if digit & 1 == 1:
            count += 1
        digit >>= 1

    return count


def count_bit2(digit: int) -> int:
    count = 0
    while digit > 0:
        count += 1
        digit &= digit - 1

    return count


if __name__ == "__main__":
    print(count_bit1(7))
    print(count_bit2(7))
