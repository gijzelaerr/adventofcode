from part_one import extract_nums
from re import sub
from typing import List

mapping = (
    ('one', "o1e"),
    ('two', "t2o"),
    ('three', "t3e"),
    ('four', "f4r"),
    ('five', "f5e"),
    ('six', "s6x"),
    ('seven', "s7n"),
    ('eight', "e8t"),
    ('nine', "n9e"),
)


def replacer(lines: List[str]) -> List[str]:
    results = []
    for line in lines:
        line = line.strip()
        for i in range(len(line)):  # backwards: , -1, -1):
            for str_, int_ in mapping:
                pattern = f"(^\\w{{{i}}}){str_}"
                func_ = lambda match: match.group(1) + int_
                line = sub(pattern, func_, line)
        print(line)
        results.append(line)
    return results


def main(file: str):
    replaced = replacer(open(file).readlines())
    total = extract_nums(replaced)
    print("----")
    print(f"total: {total}")


if __name__ == '__main__':
    main('input.txt')
