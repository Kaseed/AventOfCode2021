def sixth_solution():
    with open("data6.txt") as f:
        for i in f:
            lanternfish = [int(number) for number in i.split(',')]

    # print(lanternfish)

    # new_fish = 0
    # for i in range(80):
    #     for fish in range(len(lanternfish)):
    #         if lanternfish[fish] == 0:
    #             lanternfish[fish] = 6
    #             new_fish += 1
    #         else:
    #             lanternfish[fish] -= 1
    #     for born in range(new_fish):
    #         lanternfish.append(8)
    #     new_fish = 0
    #     # print(lanternfish)
    #
    # print(len(lanternfish))

    # part two
    school = [0] * 9
    for fish in lanternfish:
        school[fish] += 1
    # print(school)

    # simulation
    new_fish = 0
    fish_after_born = 0
    for i in range(256):
        for fish in range(len(school) - 1):
            if fish == 0:
                fish_after_born = school[fish]
                new_fish = school[fish]
            school[fish] = school[fish + 1]
        school[6] += fish_after_born
        school[8] = new_fish
        # print(school)

    fishes = 0
    for fish in school:
        fishes += fish
    print(fishes)


if __name__ == '__main__':
    sixth_solution()

