from collections import Counter
from enum import Enum

values = {'J': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
          '8': 8, '9': 9, 'T': 10, 'Q': 12, 'K': 13, 'A': 14}


class HandType(Enum):
    FIVE_OF_A_KIND = 6
    FOUR_OF_A_KIND = 5
    FULL_HOUSE = 4
    THREE_OF_A_KIND = 3
    TWO_PAIR = 2
    ONE_PAIR = 1
    HIGH_CARD = 0


class Hand:
    type: HandType

    def __init__(self, code):
        self.code = code
        counted = Counter(self.code)
        if len(counted) == 1:
            self.type = HandType.FIVE_OF_A_KIND
            return
        if 'J' in counted:
            jcount = counted.pop("J")
            keys = list(counted.keys())
            keys.sort(key=lambda x: counted[x])
            counted[keys[-1]] += jcount

        values = sorted(counted.values())
        if values == [5]:
            self.type = HandType.FIVE_OF_A_KIND
        elif values == [1, 4]:
            self.type = HandType.FOUR_OF_A_KIND
        elif values == [2, 3]:
            self.type = HandType.FULL_HOUSE
        elif values == [1, 1, 3]:
            self.type = HandType.THREE_OF_A_KIND
        elif values == [1, 2, 2]:
            self.type = HandType.TWO_PAIR
        elif values == [1, 1, 1, 2]:
            self.type = HandType.ONE_PAIR
        elif values == [1, 1, 1, 1, 1]:
            self.type = HandType.HIGH_CARD
        else:
            raise Exception("card")

    def __repr__(self):
        return "".join(self.code)

    def __lt__(self, other):
        if self.type.value == other.type.value:
            for a, b in zip(self.code, other.code):
                if values[a] == values[b]:
                    continue
                return values[a] < values[b]

        return self.type.value < other.type.value


def main(file):
    hands = []
    for row in open(file).readlines():
        hand, bid = row.split()
        hands.append((Hand(hand), int(bid)))

    hands.sort(key=lambda x: x[0])
    return hands


print(f"""
32T3K is still the only one pair; it doesn't contain any jokers, so its strength doesn't increase.
KK677 is now the only two pair, making it the second-weakest hand.
T55J5, KTJJT, and QQQJA are now all four of a kind! T55J5 gets rank 3, QQQJA gets rank 4, and KTJJT gets rank 5.
With the new joker rule, the total winnings in this example are 5905.
""")
hands = main('input_test.txt')
print(hands)
results = [(b[1], a + 1) for a, b in enumerate(hands)]
print(results)
print(sum(a * b for a, b in results))
hands = main('input.txt')
print(hands)
results = [(b[1], a + 1) for a, b in enumerate(hands)]
print(results)
print(sum(a * b for a, b in results))
