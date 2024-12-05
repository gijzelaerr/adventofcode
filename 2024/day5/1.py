from collections import defaultdict as dd


def f(p):
    rules, updates = [x.split() for x in open(p).read().split('\n\n')]

    forward = dd(list)
    for order in rules:
        b, a = order.split('|')
        forward[int(b)].append(int(a))

    for row in updates:
        t = []
        row = list(map(int, row.split(',')))
        for i in range(len(row) - 1):
            t.append(set(row[i + 1:]).issubset(set(forward[row[i]])))

        if all(t):
            yield row[len(row) // 2]



print(sum(f("test.txt")))  # should be 143
print(sum(f("input.txt")))
