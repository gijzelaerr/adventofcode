import numpy as np


def is_safe(l):
    b = np.diff(np.array(l.split(), dtype=int))
    return np.all((b >= 1) & (b < 4)) | np.all((b > -4) & (b <= -1))


def f(p):
    return sum(is_safe(l) for l in open(p))


print(f('test.txt'))
print(f('input.txt'))
