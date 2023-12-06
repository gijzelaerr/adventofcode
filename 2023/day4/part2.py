def doit(file: str):
    scores = []
    for line in open(file).readlines():
        card_str, other_str = line.split(':')
        winning_str, mine_str = other_str.split('|')
        scores.append(len(set(winning_str.split()).intersection(set(mine_str.split()))))

    card_nums = [1] * len(scores)
    for pos, score in enumerate(scores):
        card_num = card_nums[pos]
        card_nums[pos + 1:pos + score + 1] = [i + card_num for i in card_nums[pos + 1:pos + score + 1]]
    return card_nums


print("test: should be \n[1, 2, 4, 8, 14, 1] 30 ")
result = doit('input_test.txt')
print(result, sum(result))
print("------")
result = doit('input.txt')
print(result, sum(result))
