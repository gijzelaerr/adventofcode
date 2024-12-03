import numpy as np


def f(p):
    a = np.sort(np.loadtxt(p, dtype=int), axis=0)
    return np.sum(np.abs(a[:, 0] - a[:, 1]))


print(f('test.txt'))
print(f('input.txt'))
