from numpy import array, diff, delete


def safe(b):
    return all((b >= 1) & (b < 4)) | all((b > -4) & (b <= -1))


def f(p):
    for line in open(p):
        b = array(line.split(), dtype=int)
        if safe(diff(b)):
            yield True
        else:
            for i in range(b.size):
                if safe(diff(delete(b, i))):
                    yield True
                    break
            yield False


print(sum(f('test.txt')))
print(sum(f('input.txt')))
