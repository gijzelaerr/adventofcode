from numpy import array, diag, flip

S = "'X', 'M', 'A', 'S'"


def c(a):
    return repr(a).count(S)


def f(p):
    a = array([list(l.strip()) for l in open(p).readlines()])
    yield c(a)
    yield c(flip(a, 1))
    yield c(a.T)
    yield c(flip(a.T, 1))
    for i in range(a.shape[1] - 1, -a.shape[0], -1):
        print(flip(diag(a, i)))
        yield c(diag(a, i))
        yield c(flip(diag(a, i)))
        yield c(diag(flip(a, 1), i))
        yield c(flip(diag(flip(a, 1), i)))


print(sum(f('test2.txt')))  # should give 18
print(sum(f('input.txt')))
