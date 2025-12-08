import time


FILENAME = "input.txt"
PART = 2
BATTERIES = 2 if PART == 1 else 12


def getMaxJoltage(bank):
    """
    Get the maximum joltage of a battery bank by turning on a set amount of batteries. The batteries that are turned on
    are concatenated to form the joltage output: for example, the maximum joltage output of bank "28134" when turning on
    two batteries is 84, as the 2nd battery '8' and the 5th battery '4' are turned on.

    :param bank: a numeric string, with each character representing a battery
    :return: the maximum joltage output of the battery bank
    """
    max_joltage = ["0"] * BATTERIES

    current_idx = -1
    for i in range(BATTERIES):
        # The last valid position is such that every battery after it in the bank would be selected.
        last_valid_position = len(bank) - ((BATTERIES - i) - 1)
        for j in range(current_idx + 1, last_valid_position):
            if int(bank[j]) > int(max_joltage[i]):
                max_joltage[i] = bank[j]
                current_idx = j

            if max_joltage[i] == "9":
                break

    return int("".join(max_joltage))


def main(sequence):
    """
    For a sequence of battery banks, get the maximum joltage of each and sum them together.

    :param sequence: a list of numeric strings representing battery banks
    :return: the sum of the battery banks' maximum joltage outputs
    """
    total_output = 0
    for bank in sequence:
        total_output += getMaxJoltage(bank)

    return total_output


if __name__ == "__main__":
    start_time = time.time()
    with open(FILENAME) as f:
        fileContents = f.read()
        sequence = fileContents.split("\n")
        print(main(sequence))

    print(f"Time elapsed: {time.time() - start_time}s")
