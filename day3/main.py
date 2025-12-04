import math
import time


FILENAME = "input.txt"
PART = 1


def getMaxJoltage(bank):
    """
    Get the maximum joltage of a battery bank by turning on two batteries. The batteries that are turned on are
    concatenated to form the joltage output: for example, the maximum joltage output of bank "28134" is 84, as the 2nd
    battery '8' and the 5th battery '4' are turned on.

    :param bank: a numeric string, with each character representing a battery
    :return: the maximum joltage output of the battery bank
    """
    max_joltage = 0
    joltage_index = 0
    # Select first battery
    for i in range(len(bank) - 1):
        current_joltage = int(bank[i]) * 10
        if current_joltage > max_joltage:
            max_joltage = current_joltage
            joltage_index = i

        if max_joltage == 90:
            break

    # Select second battery to the right of the first one
    for j in range(joltage_index + 1, len(bank)):
        # Round max joltage down to nearest 10 before adding current joltage
        current_joltage = int(math.floor(max_joltage / 10)) * 10 + int(bank[j])
        if current_joltage > max_joltage:
            max_joltage = current_joltage

        if max_joltage == 99:
            break

    return max_joltage


def __main__(sequence):
    total_output = 0
    for bank in sequence:
        total_output += getMaxJoltage(bank)

    return total_output


if __name__ == "__main__":
    start_time = time.time()
    with open(FILENAME) as f:
        fileContents = f.read()
        sequence = fileContents.split("\n")
        print(__main__(sequence))

    print(f"Time elapsed: {time.time() - start_time}s")
