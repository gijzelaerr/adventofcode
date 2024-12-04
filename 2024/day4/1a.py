from collections import defaultdict

S = "XMAS"


def f(p):
    r = open(p).readlines()
    d = defaultdict(str) | {(y, x): r[y][x] for y in range(len(r)) for x in range(len(r[0]) - 1)}
    k = [-1, 0, 1]

    for y, x in d.copy():
        for dy, dx in [(dy, dx) for dy in k for dx in k if (dx != 0 or dy != 0)]:
            yield "".join(d[y + dy * i, x + dx * i] for i in range(len(S))) == S


print(sum(f("test1a.txt")))
print(sum(f("input.txt")))
