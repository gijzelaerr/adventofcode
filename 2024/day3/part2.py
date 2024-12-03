from re import findall

def f(p):
    total = 0
    enabled = True
    for a, b, do, dont in findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", open(p).read()):
        if do or dont:
            enabled = bool(do)
        else:
            total += int(a) * int(b) * enabled
    return total

print(f('test2.txt'))
print(f('input2.txt'))