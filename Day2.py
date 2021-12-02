def secondSolution():

    with open("data2.txt") as f:
        data = [{'position': a, 'value': int(b)} for a, b in [i.rstrip('\n').split(" ") for i in f]]

    print(data)

    horizontal = 0
    depth = 0

    for steps in data:
        if steps.get('position') == 'forward':
            horizontal += steps.get('value')
        elif steps.get('position') == 'down':
            depth += steps.get('value')
        elif steps.get('position') == 'up':
            depth -= steps.get('value')
        else:
            print("error")

    # print(horizontal)
    # print(depth)
    print(horizontal * depth)

    horizontal = 0
    depth = 0
    aim = 0

    for steps in data:
        if steps.get('position') == 'forward':
            horizontal += steps.get('value')
            depth += steps.get('value') * aim
        elif steps.get('position') == 'down':
            aim += steps.get('value')
        elif steps.get('position') == 'up':
            aim -= steps.get('value')
        else:
            print("error")

    # print(horizontal)
    # print(depth)
    print(horizontal * depth)


if __name__ == '__main__':
    secondSolution()
