import re
import time

FILENAME = "input.txt"


def isIngredientFresh(id, ranges):
    """
    Check if an ingredient ID is fresh by checking to see if it falls within an ID range.

    :param id: the numeric string ingredient ID
    :param ranges: a list of number ranges to compare the ID against
    :return: True if the ingredient falls into an ID range and is thus fresh, False otherwise
    """
    for range in ranges:
        start, end = parseIdRange(range)
        if start <= int(id) <= end:
            return True

    return False


def parseIdRange(range):
    """
    Parse a string corresponding to a range of integers into a start point and end point.

    :param range: a string following the format '<start>-<end>' where start and end are integers and end > start.
    :return: A tuple of integers (start, end)
    """
    pattern = re.compile(r"^(?P<start>[0-9]+)-(?P<end>[0-9]+)$")
    match = pattern.match(range)

    return int(match.group("start")), int(match.group("end"))


def main(ranges, ids):
    """
    Compute the number of fresh ingredients by comparing a list of ingredient IDs against a list of number ranges.

    :param ranges: a list of string number ranges in the format <start>-<end>
    :param ids: a list of numeric strings
    :return: the number of fresh ingredients
    """
    num_fresh = 0
    for id in ids:
        num_fresh += isIngredientFresh(id, ranges)

    return num_fresh


if __name__ == "__main__":
    start_time = time.time()
    with open(FILENAME) as f:
        fileContents = f.read()
        ranges, ids = fileContents.split("\n\n")
        ranges = ranges.split("\n")
        ids = ids.split("\n")
        print(main(ranges, ids))

    print(f"Time elapsed: {time.time() - start_time}s")
