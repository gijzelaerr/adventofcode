from collections import defaultdict as dd

S = list('MAS'), list('SAM')
k = -1, 0, 1
e = enumerate


def f(p):
    r = dd(str) | {(i, j): c for i, r in e(open(p)) for j, c in e(r)}
    return sum([r[i + d, j + d] for d in k] in S and [r[i + d, j - d] for d in k] in S for i, j in list(r.keys()))


print(f("test2.txt"))  # should be 9
print(f("input.txt"))
