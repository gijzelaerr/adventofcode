from itertools import product

o1 = (
    lambda a, b: a * b,
    lambda a, b: a + b,
)

o2 = o1 + (lambda a, b: int(str(a) + str(b)),)


def f(p, o=o1):
    d = {int(a): list(map(int, b.split())) for a, b in [i.split(":") for i in open(p).readlines()]}

    for k, v in d.items():
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