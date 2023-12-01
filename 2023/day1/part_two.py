from part_one import extract_nums
from re import sub
from typing import List

mapping = (
    ('one', 1),
    ('two', 2),
    ('three', 3),
    ('four', 4),
    ('five', 5),
    ('six', 6),
    ('seven', 7),
    ('eight', 8),
    ('nine', 9),
)


def replacer(lines: List[str]) -> List[str]:
    results = []
    for line in lines:
        line = line.strip()
        for i in range(len(line)):  # backwards: , -1, -1):
            for str_, int_ in mapping:
                pattern = f"(^\\w{{{i}}}){str_}"
                func_ = lambda match: match.group(1) + str(int_)
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
