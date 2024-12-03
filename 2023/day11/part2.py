from numpy import array, all, where
from itertools import combinations


def f(p, inc=10):
    a = array([list(line.strip()) for line in open(p, 'r').readlines()])
    r = where(all(a == '.', axis=1))[0]
    c = where(all(a == '.', axis=0))[0]
    for u, v in combinations(zip(*where(a == '#')), 2):
        yield abs(u[0] - v[0]) + abs(u[1] - v[1])
        yield sum([inc - 1 for b in r if min(u[0], v[0]) < b < max(u[0], v[0])])
        yield sum([inc - 1 for b in c if min(u[1], v[1]) < b < max(u[1], v[1])])


print(sum(f('test.txt', inc=10)))  # should be 1030
print(sum(f('test.txt', inc=100)))  # should be 8410
print(sum(f('input.txt', inc=1_000_000)))
