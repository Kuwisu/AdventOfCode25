import time

from day5.part1 import countFreshIngredients
from day5.part2 import countFreshIds

FILENAME = "input.txt"
PART = 2


def main(ranges, ids):
    """
    For part 1: compute the number of fresh ingredients by comparing a list of ingredient IDs against a list of number ranges.
    For part 2: compute the number of ingredient IDs considered to be fresh according to a list of number ranges.

    :param ranges: a list of string number ranges in the format <start>-<end>
    :param ids: a list of numeric strings
    :return: the number of fresh ingredients for part 1 or number of valid IDs for part 2
    """
    if PART == 1:
        return countFreshIngredients(ranges, ids)
    else:
        return countFreshIds(ranges)


if __name__ == "__main__":
    start_time = time.time()
    with open(FILENAME) as f:
        fileContents = f.read()
        ranges, ids = fileContents.split("\n\n")
        ranges = ranges.split("\n")
        ids = ids.split("\n")
        print(main(ranges, ids))

    print(f"Time elapsed: {time.time() - start_time}s")
