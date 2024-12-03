from numpy import array, all, insert, where
from itertools import combinations


def expand(a):
    r = where(all(a == '.', axis=1))[0]
    c = where(all(a == '.', axis=0))[0]
    x = array(list(a.shape[1] * '.'))

    for i, index in enumerate(r):
        a = insert(a, index + i, x, axis=0)

    y = array(list(a.shape[0] * '.'))

    for i, index in enumerate(c):
        a = insert(a, index + i, y, axis=1)

    return a


def f(p):
    a = array([list(line.strip()) for line in open(p, 'r').readlines()])
    coords = list(zip(*where(expand(a) == '#')))
    return sum(abs(u[0] - v[0]) + abs(u[1] - v[1]) for u, v in combinations(coords, 2))


print(f('test.txt'))  # == 374)
print(f('input.txt'))