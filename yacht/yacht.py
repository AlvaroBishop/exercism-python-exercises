from collections import Counter
# Score categories.
# Change the values as you see fit.
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category):
    count = Counter(dice)
    match category:
        case category if category in [ONES, TWOS, THREES, FOURS, FIVES, SIXES]:
            return category * dice.count(category)
        case category  if category == FULL_HOUSE:
            return sum(dice) if sorted(count.values()) == [2,3] else 0
        case category if category == FOUR_OF_A_KIND:
            n = 0
            for key, value in dict(count).items():
                if value >= 4:
                    n = key
            return n * 4 if n > 0 else 0
        case category if category == LITTLE_STRAIGHT:
            return 30 if sorted(dice) == [1,2,3,4,5] else 0
        case category if category == BIG_STRAIGHT:
            return 30 if sorted(dice) == [2,3,4,5, 6] else 0
        case category if category == CHOICE:
            return sum(dice)
        case category if category == YACHT:
            return 50 if len(set(dice)) == 1 else 0

            
    return 0
