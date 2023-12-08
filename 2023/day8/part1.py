def doit(file: str):
    data = open(file).read()
    moves, rest = data.split('\n\n')

    print(f"{moves=}")
    map = {}
    for line in rest.split('\n'):
        from_, to_str = [i.strip() for i in line.split('=')]
        map[from_] = to_str[1:4], to_str[6:9]

    step = 'AAA'
    counter = 0
    while True:
        step = map[step][{'L': 0, 'R': 1}[moves[counter % len(moves)]]]
        counter += 1
        if step == 'ZZZ':
            break
    return counter


result = doit('input_test.txt')
print(f"should be 2: {result}")
result = doit('input_test2.txt')
print(f"should be 6: {result}")
result = doit('input.txt')
print(f"part 1: {result}")
