import time

from day7.part1 import moveBeam
from day7.part2 import countAllTimelines

FILENAME = "input.txt"
PART = 2


def main(rows):
    """
    Part 1: compute the number of times the beam splits when navigating a beam through a tachyon manifold.
    Part 2: calculate the number of possible routes that the beam can take.

    :param rows: a list of strings representing the tachyon manifold
    :return: the number of times the beam has split
    """
    start_location = ()
    for i in range(len(rows[0])):
        if rows[0][i] == "S":
            start_location = (0, i)
            print(start_location)

    if PART == 1:
        return moveBeam(rows, *start_location)
    else:
        return countAllTimelines(rows, start_location[1])


if __name__ == '__main__':
    start_time = time.time()
    with open(FILENAME) as f:
        fileContents = f.read()
        sequence = fileContents.split("\n")
        print(main(sequence))

    print(f"Time elapsed: {time.time() - start_time}s")
