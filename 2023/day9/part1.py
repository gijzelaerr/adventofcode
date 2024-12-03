from math import comb


def doit(file):
    def recur(row):
        if all(num == 0 for num in row):
            return 0
        else:
            return row[-1] + recur([b - a for a, b in zip(row, row[1:])])

    for row in open(file).readlines():
        yield recur([int(i) for i in row.split()])


def doit2(file):
    for row in open(file).readlines():
        nums = [int(i) for i in row.split()]
        n = len(nums)
        yield sum(x * comb(n, i) * (-1) ** (n - 1 - i) for i, x in enumerate(nums))


print(list(doit('test.txt')))
print(list(doit2('test.txt')))
print("should be: [18, 28, 68] sum: 114")
print("----")
print(sum(doit('input.txt')))
print(sum(doit2('input.txt')))
