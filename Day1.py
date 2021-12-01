def firstSolution():
    data = []

    with open("data1.txt") as f:
        for i in f:
            data.append(int(i))

    print(data)

    increases = 0

    for i in range(1, len(data)):
        if data[i] > data[i - 1]:
            increases += 1

    print(increases)

    # part two
    increaseSums = 0
    sums = [data[i] + data[i-1] + data[i-2] for i in range(2, len(data))]

    print(sums)

    for i in range(1, len(sums)):
        if sums[i] > sums[i - 1]:
            increaseSums += 1

    print(increaseSums)



if __name__ == '__main__':
    firstSolution()
