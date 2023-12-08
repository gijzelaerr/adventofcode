from math import lcm


def doit(file):
    data = open(file).read()
    moves, rest = data.split('\n\n')
    map = {}
    for line in rest.split('\n'):
        from_, to_str = [i.strip() for i in line.split('=')]
        map[from_] = to_str[1:4], to_str[6:9]

    total = []
    for step in [i for i in map.keys() if i.endswith('A')]:
        counter = 0
        while True:
            if step.endswith('Z'):
                total.append(counter)
                break

            step = map[step][{'L': 0, 'R': 1}[moves[counter % len(moves)]]]
            counter += 1

    return lcm(*total)


if __name__ == '__main__':
    print(doit('input_test3.txt'))
    print(doit('input.txt'))
