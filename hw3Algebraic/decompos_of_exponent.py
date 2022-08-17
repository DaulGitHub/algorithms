# Реализовать алгоритм возведения в степень через двоичное разложение показателя степени O(2LogN) = O(LogN)

def exponent(exponent, base_of_exp) -> int:
    p = 1
    while exponent > 1:
        if exponent % 2 != 0:
            p *= base_of_exp
        exponent //= 2
        base_of_exp *= base_of_exp
    p *= base_of_exp

    return p


if __name__ == "__main__":
    N = 16
    a = 2

    res = exponent(N, a)
    print(res)
