import math
import re
import time


START_POSITION = 50
# Input file must be a series of values that fit the specifications of parseRotation, separated by new lines.
FILENAME = "input.txt"
PART = 2


def rotateDial(position, distance):
    """
    Rotates the dial according to the following rules:\n
    - Turning the dial left from 0 one click makes it point to 99, or right from 99 one click to 0.
    - PART 2 ONLY: If any click causes the dial to point to 0, it should increment the password.

    :param position: the current position of the dial
    :param distance: the number of clicks that the dial must move through
    :return: a tuple (result, clicks) where result is the position of the dial after rotation and clicks is the amount to increment the password by (for part 2).
    """
    clicks = 0
    m = -100 if distance < 0 else 100
    result = position + (distance % m)

    # For every full rotation of the dial, add a click
    if PART == 2:
        clicks += math.floor((distance / m))

    # If the result spun the dial around and the dial did not start on 0, add a click
    if PART == 2 and (100 < result or result < 0) and position != 0:
        clicks += 1

    # Compute dial spinning around from 0 to 99 or 99 to 0
    if result < 0:
        result = 100 + result
    elif result > 99:
        result = result - 100

    return result, clicks


def parseRotationCode(rotation):
    """
    Parse the number of clicks left or right that the dial must travel based on the input text according to the
    following rules:\n
    - A rotation starts with an L or R which indicates whether the rotation should toward lower or higher numbers.
    - Then, the rotation has a distance value which indicates how many clicks the dial must move in that direction.

    :param rotation: A string in the format '<direction><distance>' where direction is L or R and distance is an integer greater than 1.
    :return: An integer number of clicks for the dial to travel, negative if left and positive if right.
    """
    is_left = False
    pattern = re.compile(r"^(?P<rotation>[LR])"
                         r"(?P<distance>[0-9]+)$")
    match = pattern.match(rotation)

    if match.group("rotation") == "L":
        is_left = True

    return int(match.group("distance")) * (-1 if is_left else 1)


def main(sequence):
    """
    Rotate a dial according to a sequence of rotations and return a password computed based on the number of times the
    dial ends on 0 (for both parts) or passes 0 (only for Part 2).

    :param sequence: a list of rotation code strings fitting specifications set in parseRotationCode
    :return: the computed integer password to open the door
    """
    position = START_POSITION
    password = 0
    for rotation in sequence:
        distance = parseRotationCode(rotation)
        position, clicks = rotateDial(position, distance)

        password += clicks
        if position == 0:
            password += 1

    return password


if __name__ == "__main__":
    start_time = time.time()
    with open(FILENAME) as f:
        fileContents = f.read()
        sequence = fileContents.split("\n")
        print(main(sequence))

    print(f"Time elapsed: {time.time() - start_time}s")
