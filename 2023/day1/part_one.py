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


if __name__ == '__main__':
    total = extract_nums(open('input.txt').readlines())
    print(f"total: {total}")
