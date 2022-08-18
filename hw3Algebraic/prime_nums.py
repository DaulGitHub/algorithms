# Реализовать алгоритм поиска простых чисел с оптимизациями поиска и делением только на простые числа, O(N * Sqrt(N) / Ln (N))

prime_numbers = []


def count_nums(until_num: int) -> int:

    for i in range(2, until_num):
        if is_prime(i):
            prime_numbers.append(i)

    return len(prime_numbers)


def is_prime(n: int) -> bool:

    if n == 2:
        return True

    midle = n//2
    for prime in prime_numbers:
        if prime > midle:
            break
        if n % prime == 0:
            return False
    return True


if __name__ == "__main__":
    N = 100
    count = count_nums(N)
    print(count)
