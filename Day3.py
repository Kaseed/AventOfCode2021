def bin_to_dec(list):
    list2 = list.copy()
    list2.reverse()
    value = 0

    for i in range(len(list2)):
        if list2[i] == 1:
            value += 2 ** i
    return value


def negate_bin(list):
    return [1 if i == 0 else 0 for i in list]


def calculate_most_common_value(list, pointer):
    value = 0
    for i in list:
        if i[pointer] == '1':
            value += 1
    if value >= len(list) / 2:
        return '1'
    else:
        return '0'


def calculate_least_common_value(list, pointer):
    value = 0
    for i in list:
        if i[pointer] == '1':
            value += 1
    if value < len(list) / 2:
        return '1'
    else:
        return '0'


def delete_uncommon_value(list, common_value, pointer):
    to_delete = []
    for i in list:
        if i[pointer] != common_value:
            to_delete.append(i)

    for delete in to_delete:
        list.remove(delete)


def oxygen_generator_rating(list, pointer):
    if len(list) == 1:
        return list
    else:
        common_value = calculate_most_common_value(list, pointer)
        delete_uncommon_value(list, common_value, pointer)
        return oxygen_generator_rating(list, pointer + 1)


def co2_scrubber_rating(list, pointer):
    if len(list) == 1:
        return list
    else:
        common_value = calculate_least_common_value(list, pointer)
        delete_uncommon_value(list, common_value, pointer)
        return co2_scrubber_rating(list, pointer + 1)


def third_solution():
    with open("data3.txt") as f:
        data = [i.rstrip('\n') for i in f]

    gamma = [0] * len(data[0])

    for i in data:
        for j in range(len(gamma)):
            if i[j] == '1':
                gamma[j] += 1

    gamma = [1 if gamma[i] > len(data) / 2 else 0 for i in range(len(gamma))]

    print(gamma)

    epsilon = [1 if i == 0 else 0 for i in gamma]

    print(epsilon)

    print(bin_to_dec(gamma) * bin_to_dec(epsilon))

    number = oxygen_generator_rating(data.copy(), 0)
    print(number)

    number2 = co2_scrubber_rating(data.copy(), 0)
    print(number2)

    print(bin_to_dec([int(i) for i in number[0]]) * bin_to_dec([int(i) for i in number2[0]]))


if __name__ == '__main__':
    third_solution()
