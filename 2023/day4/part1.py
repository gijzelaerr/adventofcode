def doit(file: str):
    points = 0
    for line in open(file).readlines():
        card_str, other_str = line.split(':')
        winning_str, mine_str = other_str.split('|')
        score = len(set(winning_str.split()).intersection(set(mine_str.split())))
        points += score if not score else 2 ** (score - 1)
    return points

print("test: shold be 13")
print(doit('input_test.txt'))
print("------")
print(doit('input.txt'))
