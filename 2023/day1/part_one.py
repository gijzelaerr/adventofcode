from re import findall
from typing import List


def extract_nums(lines: List[str]):
    total = 0
    for line in lines:
        ints = findall(r'\d', line.strip())
        sum = int(ints[0] + ints[-1])
        total += sum
        print(line)
        print(f" {ints[0]} + {ints[-1]} = {sum}")
    return total


def main(file: str):
    total = extract_nums(open(file).readlines())
    print(f"total: {total}")


if __name__ == '__main__':
    main('input.txt')
