from numpy import array, unique, where
from operator import ior
from itertools import permutations
from functools import reduce


def anti(coords):
    return {(2 * x1 - x2, 2 * y1 - y2) for (x1, y1), (x2, y2) in permutations(coords, 2)}


def f(p):
    a = array([list(l.strip()) for l in open(p).readlines()])
    all_anti = reduce(ior, map(anti, (zip(*where(a == i)) for i in set(unique(a)) - {'\n', '.'})))
    return len({(i, j) for i, j in all_anti if i in range(a.shape[0]) and j in range(a.shape[1])})


print(f('test.txt'))  # should be 14
print(f('input.txt'))
