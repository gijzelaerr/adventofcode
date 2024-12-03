import numpy as np


def is_safe(b):
    return np.all((b >= 1) & (b < 4)) | np.all((b > -4) & (b <= -1))


def f(p):
    for line in open(p):
        b = np.array(line.split(), dtype=int)
        if is_safe(np.diff(b)):
            yield True
        else:
            for i in range(b.size):
                if is_safe(np.diff(np.delete(b, i))):
                    yield True
                    break
            yield False


print(sum(f('test.txt')))
print(sum(f('input.txt')))
