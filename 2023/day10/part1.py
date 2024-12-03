from queue import Queue

mapping = {
    "|": [(0, -1), (0, 1)],
    "-": [(-1, 0), (1, 0)],
    "L": [(0, -1), (1, 0)],
    "J": [(0, -1), (-1, 0)],
    "7": [(-1, 0), (0, 1)],
    "F": [(1, 0), (0, 1)],
}


def doit1(file):
    lines = [l.strip() for l in open(file, "r")]
    x, y = None, None
    q = Queue()

    for yi, line in enumerate(lines):
        for xi, c in enumerate(line):
            if c == "S":
                x, y = xi, yi
                break

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        c = lines[y + dy][x + dx]
        if c in mapping:
            for dx2, dy2 in mapping[c]:
                if x == x + dx + dx2 and y == y + dy + dy2:
                    q.put((1, (x + dx, y + dy)))

    dists = {(x, y): 0}

    while not q.empty():
        d, (x, y) = q.get()

        if (x, y) in dists:
            continue

        dists[(x, y)] = d

        for dx, dy in mapping[lines[y][x]]:
            q.put((d + 1, (x + dx, y + dy)))
    return dists

if __name__ == '__main__':
    print("test: should be 4")
    dists = doit1('test.txt')
    print(f"Part 1: {max(dists.values())}")
    dists = doit1('input.txt')
    print(f"Part 1: {max(dists.values())}")
