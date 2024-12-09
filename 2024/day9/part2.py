from collections import deque


def f(p):
    q = deque([])
    empty = deque([])
    id_, pos = 0, 0
    disk = []
    for i, c in enumerate(open(p).read().strip()):
        if i % 2 == 0:
            q.append((pos, int(c), id_))
            for _ in range(int(c)):
                disk.append(id_)
                pos += 1
            id_ += 1
        else:
            empty.append((pos, int(c)))
            for _ in range(int(c)):
                disk.append(0)
                pos += 1

    for (pos, sz, id_) in reversed(q):
        for s_i, (s_pos, s_sz) in enumerate(empty):
            if s_pos < pos and sz <= s_sz:
                for i in range(sz):
                    disk[pos + i] = 0
                    disk[s_pos + i] = id_
                empty[s_i] = (s_pos + sz, s_sz - sz)
                break

    return sum(i * c for i, c in enumerate(disk))


print(f('test.txt'))  # should be 2858
print(f('input.txt'))
