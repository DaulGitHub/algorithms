def recursive(number: int) -> int:
    if number == 1 or number == 2:
        return number - 1
    else:
        return recursive(number - 1) + recursive(number - 2)


def iterative(number: int) -> int:
    i = 1
    while i <= number:
        if i == 1:
            fib = 0
        elif i == 2:
            fib = 1
            fib1 = 0
        elif i > 2:
            fib2 = fib
            fib = fib + fib1
            fib1 = fib2
        i += 1

    return fib


if __name__ == "__main__":
    n = 9
    res_recursive = recursive(n)
    res_iter = iterative(n)
    print("res_recursive is {}".format(res_recursive))
    print("res_iter is {}".format(res_iter))
