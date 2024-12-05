from functools import cmp_to_key


def f(p):
    rules_str, updates_str = open(p).read().split("\n\n")
    rules = set(map(lambda s: tuple(map(int, s.split("|"))), rules_str.splitlines()))
    updates = list(map(lambda s: list(map(int, s.split(","))), updates_str.splitlines()))

    def cmp(a, b):
        return int((b, a) in rules) - int((a, b) in rules)

    r = [0, 0]

    for update in updates:
        fixed_update = sorted(update, key=cmp_to_key(cmp))
        r[fixed_update != update] += fixed_update[len(fixed_update) // 2]

    return r


print(f("test.txt"))
print(f("input.txt"))
