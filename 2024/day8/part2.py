from numpy import array, unique, where
from itertools import combinations
from operator import ior
from functools import reduce


def anti(coords1, coords2, w, h):
    x1, y1 = coords1
    x2, y2 = coords2
    dx, dy = x2 - x1, y2 - y1
    xa, ya = x1, y1
    while xa in range(w) and ya in range(h):
        yield xa, ya
        xa, ya = xa + dx, ya + dy
    xa, ya = x1, y1
    while xa in range(w) and ya in range(h):
        yield xa, ya
        xa, ya = xa - dx, ya - dy


def f(p):
    a = array([list(l.strip()) for l in open(p).readlines()])
    w, h = a.shape
    freq_coords = (zip(*where(a == i)) for i in set(unique(a)) - {'\n', '.'})
    return len(reduce(ior, [reduce(ior, (set(anti(c1, c2, w, h)) for c1, c2 in combinations(coords, 2))) for coords in
                            freq_coords]))


print(f('test.txt'))  # should be 14
print(f('input.txt'))
