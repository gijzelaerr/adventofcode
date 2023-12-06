def doit(file: str):
    a, b = open(file).readlines()
    time = int("".join(a.split()[1:]))
    record = int("".join(b.split()[1:]))

    win = 0
    for hold in range(time + 1):
        if hold * (time - hold) > record:
            win += 1
    print(win)


doit('input_test.txt')
doit('input.txt')
