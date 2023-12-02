def doit_return_cubes(file: str):
    powers = []
    for line in open(file).readlines():
        game_str, draw_str = line.split(":")
        game = int(game_str.strip().split()[1])
        draws = draw_str.strip().split(';')
        min_blue = min_red = min_green = 0
        for draw in draws:
            for cube in draw.split(','):
                count, color = cube.strip().split()
                count = int(count)
                if color == 'blue':
                    if count > min_blue:
                        min_blue = count
                elif color == 'red':
                    if count > min_red:
                        min_red = count
                elif color == 'green':
                    if count > min_green:
                        min_green = count
                else:
                    raise Exception
            print(f"\t{min_blue=}\t{min_red=}\t{min_green=}")
        if min_blue == 0 or min_red == 0 or min_green == 0:
            raise Exception
        powers.append(min_blue*min_red*min_green)
    return powers


print("test")
valid_games = doit_return_cubes('input_test.txt')
print(valid_games)
print("should be 48, 12, 1560, 630,  36")
print(f"sum: {sum(valid_games)}")

print("------\nproduction")
valid_games = doit_return_cubes('input.txt')
print(valid_games)
print(sum(int(i) for i in valid_games))