from re import compile

c = compile(r"mul\((\d{0,3}),(\d{0,3})\)|(do\(\))|(don't\(\))")


def f(p):
    total = 0
    enabled = True
    for a, b, do, dont in c.findall(open(p).read()):
        if do or dont:
            enabled = bool(do)
        else:
            total += int(a) * int(b) * enabled
    return total


print(f('test2.txt'))
print(f('input2.txt'))
