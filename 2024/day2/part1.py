from numpy import diff, array, all


def safe(l):
    b = diff(array(l.split(), dtype=int))
    return all((b >= 1) & (b < 4)) | all((b > -4) & (b <= -1))


def f(p):
    return sum(safe(l) for l in open(p))


print(f('test.txt'))
print(f('input.txt'))
