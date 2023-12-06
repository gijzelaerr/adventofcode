


order = [
    'seed-to-soil',
    'soil-to-fertilizer',
    'fertilizer-to-water',
    'water-to-light',
    'light-to-temperature',
    'temperature-to-humidity',
    'humidity-to-location'
]

def double_pairs(l):
    from itertools import groupby
    x = [list(group) for index, group in groupby(enumerate(l), lambda x: x[0] // 2)]
    return [i[1] for i in x]


def extract_data(file: str):
    lines = open(file).read()
    seeds = []
    maps = {}
    for group in lines.split('\n\n'):
        label, value_lines = group.split(':')
        label = label.strip()
        value_lines = value_lines.strip()

        if label == 'seeds':
            seeds = [int(i) for i in value_lines.split()]
        else:
            map_type = label.split()[0]
            maps[map_type] = []
            for value_line in value_lines.split('\n'):
                dest_range_start, src_range_start, range_len = [int(i) for i in value_line.split()]
                maps[map_type].append((dest_range_start, src_range_start, range_len))
    return seeds, maps


def main(file):
    seeds, maps = extract_data(file)
    lowest = -1
    for i in range(0, len(seeds), 2):
        start = seeds[i]
        number = seeds[i+1]
        for seed in range(start, start+number):
            next_from = seed
            path = []
            for step in order:
                will_be_next = None
                for line in maps[step]:
                    dest_range_start, src_range_start, range_len = line
                    if src_range_start <= next_from <= src_range_start + range_len:
                        will_be_next = dest_range_start + next_from - src_range_start
                        break
                if will_be_next:
                    next_from = will_be_next
                path.append(next_from)
            if lowest > path[-1] or lowest == -1:
                lowest = path[-1]
    return lowest


def min_location(results):
    return min(i[-1] for i in results.values())



print("""test, answer should be:
lowest location is 46
-----
""")
print(main('input_test.txt'))

print("----")
print(main('input.txt'))
