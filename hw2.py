if __name__ == "__main__":

    amount = 0
    for i in range(1000):
        sum1 = sum([int(j) for j in list(str(i))])
        for k in range(1000):
            sum2 = sum([int(j) for j in list(str(k))])
            if sum1 == sum2:
                amount += 1

    print(amount)
