import numpy as np

def is_safe(b):
    return np.all((b >= 1) & (b < 4)) | np.all((b > -4) & (b <= -1))

def f(p):
    safes = []
    for line in open(p):
        b = np.array(line.split(), dtype=int)
        if is_safe(np.diff(b)):
            safes.append(True)
        else:
            for i in range(b.size):
                c = np.delete(b, i)
                if is_safe(np.diff(c)):
                    safes.append(True)
                    break
            safes.append(False)
    return np.sum(np.array(safes))


print(f('test.txt'))
print(f('input.txt'))