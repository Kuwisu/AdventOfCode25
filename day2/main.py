import re
import time


FILENAME = "input.txt"
PART = 2


def isIdValid(id):
    """
    Compute whether an ID is valid, where invalid IDs are composed of multiple sequences of repeating numbers
    (for Part 1, this is limited to 2).

    :param id: an integer ID to evaluate
    :return: True if the ID is valid, False otherwise
    """
    id_string = str(id)
    length = len(id_string)
    num_slices = 2

    # Evaluate every way of evenly slicing the string
    while num_slices <= length:
        if length % num_slices == 0:
            # Cut the string into a set of slices and check them for equality
            seq_value = -1
            is_sequence_valid = False
            for i in range(num_slices):
                start = int((length / num_slices) * i)
                end = int((length / num_slices) * (i + 1))
                slice_value = id_string[start:end]

                # If the segment differs from a previous segment, the ID is valid
                if seq_value == -1:
                    seq_value = slice_value
                elif seq_value != slice_value:
                    is_sequence_valid = True
                    break

            if not is_sequence_valid:
                return False

        # To solve part 1, only evaluate 2 slices
        if PART == 1:
            break

        num_slices += 1

    return True


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
    for num_range in sequence:
        start, end = parseIdRange(num_range)
        invalid_list.extend(getInvalidIdsInRange(start, end))

    return sum(invalid_list)


if __name__ == "__main__":
    start_time = time.time()
    with open(FILENAME) as f:
        fileContents = f.read()
        sequence = fileContents.split(",")
        print(__main__(sequence))

    print(f"Time elapsed: {time.time() - start_time}s")
