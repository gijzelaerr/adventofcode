from numpy import loadtxt, array, sum, multiply


def f(p):
    a = loadtxt(p, dtype=int)
    b = array([sum(i == a[:, 1]) for i in a[:, 0]])
    return sum(multiply(a[:, 0], b))


print(f('test.txt'))
print(f('input.txt'))
