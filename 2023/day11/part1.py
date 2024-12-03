from itertools import combinations
from typing import Tuple, List

type Row = List[int]
type Square = List[Row]
type Galaxy = Tuple[int, int]


def find_empty(lines: Square) -> List[int]:
    empty = []
    current = 0
    for i, line in enumerate(lines):
        if "#" not in line:
            current += 1
        empty.append(current)
    return empty


def transpose(lines: Square) -> Square:
    return list(zip(*lines))


def find_galaxies(lines: Square) -> List[Galaxy]:
    galaxies: List[Galaxy] = []
    for j, row in enumerate(lines):
        for i, c in enumerate(row):
            if c == "#":
                galaxies.append((j, i))
    return galaxies


def manhatten(a0: int, a1: int, b0: int, b1: int, empty_rows: List[int], empty_cols: List[int], expand: int):
    return abs(b0 - a0) + abs(b1 - a1) + \
        (expand - 1) * (empty_rows[max(b0, a0)] - empty_rows[min(b0, a0)]) + \
        (expand - 1) * (empty_cols[max(b1, a1)] - empty_cols[min(b1, a1)])


def all_distances(galaxies: List[Galaxy], empty_rows: List[int], empty_cols: List[int], expand: int):
    return sum(manhatten(a0, a1, b0, b1, empty_rows, empty_cols, expand)
               for (a0, a1), (b0, b1) in combinations(galaxies, 2))


def doit(file):
    lines: Square = [line.strip() for line in open(file).readlines()]

    empty_rows = find_empty(lines)
    empty_cols = find_empty(transpose(lines))
    galaxies = find_galaxies(lines)
    result = all_distances(galaxies, empty_rows, empty_cols, 2)
    print(f"part1: {result}")
    result = all_distances(galaxies, empty_rows, empty_cols, 1000000)
    print(f"part2: {result}")


print("test, should be 374")
doit('test.txt')
print("------")
doit('input.txt')
