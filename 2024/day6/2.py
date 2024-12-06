def walk(G, start, part=1):
    pos, dir = start, -1
    seen = set()
    while pos in G and (pos, dir) not in seen:
        seen |= {(pos, dir)}
        if G.get(pos + dir) == "#":
            dir *= -1j
        else:
            pos += dir
    if part:
        return (pos, dir) in seen
    else:
        return {pos for pos, _ in seen}


def f(p):
    a = {i + j * 1j: c for i, r in enumerate(open(p))
         for j, c in enumerate(r.strip())}

    start = min(p for p in a if a[p] == '^')

    path = walk(a, start, 0)
    print(f"1: {len(path)}")
    print(f"2: {sum(walk(a | {o: '#'}, start) for o in path)}")


f('test.txt')
f('input.txt')
