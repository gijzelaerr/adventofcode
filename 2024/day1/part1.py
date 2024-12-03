from numpy import sort, loadtxt, sum, abs


def f(p):
    a = sort(loadtxt(p, dtype=int), axis=0)
    return sum(abs(a[:, 0] - a[:, 1]))


print(f('test.txt'))
print(f('input.txt'))
