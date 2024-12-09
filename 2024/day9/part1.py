from collections import deque


def f(p):
    q = deque([])
    empty = deque([])
    id_ = 0
    disk = []
    pos = 0
    for i, c in enumerate(open(p).read().strip()):
        if i % 2 == 0:
            for _ in range(int(c)):
                disk.append(id_)
                q.append((pos, id_))
                pos += 1
            id_ += 1
        else:
            empty.append((pos, int(c)))
            for _ in range(int(c)):
                disk.append(0)
                pos += 1

    for pos, id_ in reversed(q):
        for space_i, (space_pos, space_sz) in enumerate(empty):
            if space_pos < pos and space_sz >= 1:
                disk[pos] = 0
                disk[space_pos] = id_
                empty[space_i] = (space_pos + 1, space_sz - 1)
                break

    return sum([i * c for i, c in enumerate(disk)])


print(f('test.txt'))  # should be 1928
print(f('input.txt'))
