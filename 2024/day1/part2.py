import numpy as np


def f(p):
    a = np.loadtxt(p, dtype=int)
    b = np.array([np.sum(i == a[:, 1]) for i in a[:, 0]])
    return np.sum(np.multiply(a[:, 0], b))


print(f('test.txt'))
print(f('input.txt'))
