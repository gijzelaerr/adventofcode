from re import compile

c = compile(r'mul\((\d{0,3}),(\d{0,3})\)')

def f(p):
    return sum(int(a) * int(b) for a, b in  c.findall(open(p).read()))

print(f('test.txt'))
print(f('input.txt'))