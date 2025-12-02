import re


FILENAME = "input.txt"


def isIdValid(id):
    """
    Compute whether an ID is valid, where invalid IDs are composed of two sequences of repeating numbers.

    :param id: an integer ID to evaluate
    :return: True if the ID is valid, False otherwise
    """
    id_string = str(id)
    length = len(id_string)
    if length % 2 != 0:
        return True
    else:
        seq_1 = (id_string[:int(length / 2)])
        seq_2 = (id_string[int(length / 2):])
        return seq_1 != seq_2


def getInvalidIdsInRange(start, end):
    """
    Iterate over a range of integers and return all that are invalid IDs.

    :param start: the start value of iteration
    :param end: the end value of iteration
    :return: a list of integer IDs that were computed to be invalid
    """
    invalid_list = []
    for i in range(start, end + 1):
        if not isIdValid(i):
            invalid_list.append(i)

    return invalid_list


def parseIdRange(range):
    """
    Parse a string corresponding to a range of integers into a start point and end point.

    :param range: a string following the format '<start>-<end>' where start and end are integers and end > start.
    :return: A tuple of integers (start, end)
    """
    pattern = re.compile(r"^(?P<start>[0-9]+)-(?P<end>[0-9]+)$")
    match = pattern.match(range)

    return int(match.group("start")), int(match.group("end"))


def __main__(sequence):
    """
    Return the sum of every invalid integer in a sequence of integer ranges. Invalid integers are composed of two
    sequences of repeating numbers.

    :param sequence: a list of string integer ranges to iterate through
    :return: the sum of invalid integers
    """
    invalid_list = []
    for range in sequence:
        start, end = parseIdRange(range)
        invalid_list.extend(getInvalidIdsInRange(start, end))

    return sum(invalid_list)


if __name__ == "__main__":
    with open(FILENAME) as f:
        fileContents = f.read()
        sequence = fileContents.split(",")
        print(__main__(sequence))
