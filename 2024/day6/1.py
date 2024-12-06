from numpy import array, where, flip

dirs = {
    '^': (-1, 0, '>', lambda a, p: flip(a[:p[0], p[1]])),
    '>': (0, 1, 'v', lambda a, p: a[p[0], p[1] + 1:]),
    'v': (1, 0, '<', lambda a, p: a[p[0] + 1:, p[1]]),
    '<': (0, -1, '^', lambda a, p: flip(a[p[0], :p[1]]))
}


def f(p):
    a = array([list(l.strip()) for l in open(p).readlines()])
    ori = '^'
    pos = tuple(i[0] for i in where(a == ori))
    v = set(pos)

    while True:
        dx, dy, next, gp = dirs[ori]
        path = gp(a, pos)
        end = where(path == '#')[0]
        if not len(end):
            steps = len(path)
        else:
            steps = end[0]
        for i in range(steps):
            v |= {pos := (pos[0] + dx, pos[1] + dy)}
        if not len(end):
            break
        ori = next

    return len(set(v))


print(f('test.txt'))
print(f('input.txt'))
