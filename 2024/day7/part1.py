from itertools import product
from operator import add, mul

o1 = (add, mul)

o2 = o1 + (lambda a, b: int(str(a) + str(b)),)


def f(p, o=o1):
    for l in open(p):
        x = l.split()
        x[0] = x[0][:-1]
        k, *v = map(int, x)

        for x in product(o, repeat=len(v) - 1):
            cursor = v[0]
            for i in range(len(x)):
                cursor = x[i](cursor, v[i + 1])
            if k == cursor:
                yield k
                break


print(sum(f('test.txt')))  # should be 3749
print(sum(f('input.txt')))

print(sum(f('test.txt', o=o2)))  # should be 11387
print(sum(f('input.txt', o=o2)))
