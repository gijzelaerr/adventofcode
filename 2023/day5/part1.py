

order = [
    'seed-to-soil',
    'soil-to-fertilizer',
    'fertilizer-to-water',
    'water-to-light',
    'light-to-temperature',
    'temperature-to-humidity',
    'humidity-to-location'
]


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
    results = {}
    for seed in seeds:
        next_from = seed

        path = []
        for step in order:
            #print(f"step: {step}")
            match = False
            will_be_next = None
            for line in maps[step]:
                dest_range_start, src_range_start, range_len = line
                if step == 'fertilizer-to-water':
                    ...
                if src_range_start <= next_from <= src_range_start + range_len:
                    if match:
                        print("double match")
                        if will_be_next != (dest_range_start + next_from - src_range_start):
                            print(f"conflict: {will_be_next} & {dest_range_start + next_from - src_range_start}")
                    else:
                        match = True
                        will_be_next = dest_range_start + next_from - src_range_start
                        #print(f"match: {will_be_next}")
            if not will_be_next:
                ...
                #print(f"no match so keeping the same number {next_from}")
            else:
                next_from = will_be_next
            path.append(next_from)
        results[seed] = path
    return results


def min_location(results):
    return min(i[-1] for i in results.values())


print("""test, answer should be:
Seed 79, soil 81, fertilizer 81, water 81, light 74, temperature 78, humidity 78, location 82.
Seed 14, soil 14, fertilizer 53, water 49, light 42, temperature 42, humidity 43, location 43.
Seed 55, soil 57, fertilizer 57, water 53, light 46, temperature 82, humidity 82, location 86.
Seed 13, soil 13, fertilizer 52, water 41, light 34, temperature 34, humidity 35, location 35.
lowest location number is 35.
-----
""")
results = main('input_test.txt')
print(results)
print(min_location(results))

results = main('input.txt')
print(results)
print(min_location(results))