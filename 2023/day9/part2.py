from math import comb


def doit(file):
    def recur(row):
        if all(num == 0 for num in row):
            return 0
        else:
            return row[0] - recur([b - a for a, b in zip(row, row[1:])])

    for row in open(file).readlines():
        yield recur([int(i) for i in row.split()])


def doit2(file):
    for line in open(file).readlines():
        row = list(map(int, line.split()))
        n = len(row)
        yield sum(x * comb(n, i + 1) * (-1) ** i for i, x in enumerate(row))


print(list(doit('input_test.txt')))
print(list(doit2('input_test.txt')))
print("should be: [5, -3, 0] sum: 2")
print("----")
print(sum(doit('input.txt')))
print(sum(doit2('input.txt')))
