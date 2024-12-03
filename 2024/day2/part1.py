import numpy as np

def f(p):
    safes = []
    for line in open(p):
        b = np.diff(np.array(line.split(), dtype=int))
        safe = np.all((b >= 1) & (b < 4)) | np.all((b > -4) & (b <= -1))
        safes.append(safe)
    return np.sum(np.array(safes))


print(f('test.txt'))
print(f('input.txt'))