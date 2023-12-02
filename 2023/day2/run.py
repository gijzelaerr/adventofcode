def doit(file: str, max_red: int, max_green: int, max_blue: int):
    valid_games = []
    for line in open(file).readlines():
        game_str, draw_str = line.split(":")
        game = game_str.strip().split()[1]
        draws = draw_str.strip().split(';')
        print(game)
        blue = red = green = 0
        for draw in draws:
            for cube in draw.split(','):
                count, color = cube.strip().split()
                if color == 'blue':
                    blue += int(count)
                elif color == 'red':
                    red += int(count)
                elif color == 'green':
                    green += int(count)
        print(f"{blue=}\t{red=}\t{green=}")
        if blue <= max_blue and green <= max_green and red <= max_red:
            valid_games.append(game)
    return valid_games

print("test")
valid_games = doit('input_test.txt', max_red=12, max_green=13, max_blue=14)
print(valid_games)
print("should be 1, 2, and 5")

print("------\nproduction")
valid_games = doit('input.txt', max_red=12, max_green=13, max_blue=14)
print(valid_games)
print(sum(int(i) for i in valid_games))
