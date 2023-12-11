from part1 import doit1


def doit(file):
    lines = [l.strip() for l in open(file, "r")]

    w = len(lines[0])
    h = len(lines)

    dists = doit1(file)

    inside = 0
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if (x, y) in dists:
                continue

            crosses = 0
            x2, y2 = x, y

            while x2 < w and y2 < h:
                c2 = lines[y2][x2]
                if (x2, y2) in dists and c2 != "L" and c2 != "7":
                    crosses += 1
                x2 += 1
                y2 += 1

            if crosses % 2 == 1:
                inside += 1

    return inside


print("test: should be 10")
results = doit('input_test.txt')
print(f"Part 2: {results}")
results = doit('input.txt')
print(f"Part 2: {results}")
