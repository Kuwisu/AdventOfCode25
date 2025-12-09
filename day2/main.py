import time

from utils import parseIdRange

FILENAME = "input.txt"
PART = 2


def areSegmentsEqual(string, num_segments):
    """
    Determine whether all segments are equal for a number string segmented into even parts.

    :param string: a string containing the number to evaluate
    :param num_segments: the number of segments to split the string into
    :return: True if all segments are equal, false otherwise
    """
    first_segment = -1
    for i in range(num_segments):
        start = int((len(string) / num_segments) * i)
        end = int((len(string) / num_segments) * (i + 1))
        segment = string[start:end]

        if first_segment == -1:
            first_segment = segment
        elif segment != first_segment:
            return False

    return True


def isIdValid(id):
    """
    Compute whether an ID is valid, where invalid IDs are composed of multiple segments of repeating numbers
    (for Part 1, this is limited to 2 segments).

    :param id: an integer ID to evaluate
    :return: True if the ID is valid, False otherwise
    """
    id_string = str(id)
    num_segments = 2

    # Evaluate every way of evenly segmenting the string for equality
    while num_segments <= len(id_string):
        if len(id_string) % num_segments == 0 and areSegmentsEqual(id_string, num_segments):
            return False

        # To solve part 1, only evaluate 2 segments
        if PART == 1:
            break

        num_segments += 1

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


def main(sequence):
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
        print(main(sequence))

    print(f"Time elapsed: {time.time() - start_time}s")
