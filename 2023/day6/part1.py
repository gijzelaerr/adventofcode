def doit(file: str):
    time, distance = open(file).readlines()
    times = [int(i) for i in time.split()[1:]]
    records = [int(i) for i in distance.split()[1:]]

    wins = 1
    for t, r in zip(times, records):
        win = 0
        for hold in range(t + 1):
            if hold * (t - hold) > r:
                win += 1
        wins *= win
    print(wins)


doit('input_test.txt')
doit('input.txt')
