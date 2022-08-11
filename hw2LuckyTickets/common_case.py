
def lucky_tickets_combinations(digits: int) -> list:
    vertica_max_index = 9
    horizontal_max_index = 9 * digits

    combination_t = []
    if digits == 1:
        for i in range(vertica_max_index+1):
            combination_t.append([1 if k == i else 0 for k in range(horizontal_max_index+1)])
        return calc_sums(combination_t, horizontal_max_index)
    elif digits > 1:
        sum_of_combinations = lucky_tickets_combinations(digits-1)
        for i in range(vertica_max_index+1):
            combination_t.append([])
            for j in range(horizontal_max_index+1):
                if j < i:
                    combination_t[i].append(0)
                elif j >= len(sum_of_combinations)+i:
                    combination_t[i].append(0)
                else:
                    combination_t[i].append(sum_of_combinations[j-i])

        return calc_sums(combination_t, horizontal_max_index)


def calc_sums(table: list, horizontal_max_index: int) -> list:
    result = []
    for k in range(horizontal_max_index+1):
        sum_of_combinations = 0
        for i in range(10):
            sum_of_combinations += table[i][k]
        result.append(sum_of_combinations)

    return result


if __name__ == "__main__":
    digits = 5

    sum_of_combinations = lucky_tickets_combinations(digits)
    lucky_tickets_num = sum([i*i for i in sum_of_combinations])
    print("lucky_tickets_num = {}".format(lucky_tickets_num))

