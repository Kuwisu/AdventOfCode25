import time

FILENAME = "input.txt"
PART = 1
ROWS = 4 if FILENAME == "exampleInput.txt" else 5


def parseProblemRow(row):
    """
    Convert a string of spaced numbers to a list of integers.

    :param row: a string of spaced integers
    :return: a list of integers
    """
    # Remove leading space
    if row[0] == " ":
        row = row[1:]

    return [int(num) for num in row.split(" ")]


def addColumn(numbers):
    """
    Add a tuple of integers together.

    :param numbers: a tuple of integers to add
    :return: the total sum
    """
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]

    return total


def multiplyColumn(numbers):
    """
    Multiply a tuple of integers together.

    :param numbers: a tuple of integers to multiply
    :return: the total product
    """
    total = 1
    for i in range(len(numbers)):
        total = total * numbers[i]

    return total


def main(problem_rows):
    """
    Solve a mathematical problem sheet by summing or multiplying columns and adding the results together.

    :param problem_rows: a list of ROWS-1 strings of spaced numbers and a string of spaced mathematical operators
    :return: the total sum
    """
    problem_symbols = problem_rows[ROWS-1].split(" ")
    problem_numbers = []
    sum = 0
    for i in range(ROWS - 1):
        problem_numbers.append(parseProblemRow(problem_rows[i]))

    # Solve each problem in the sheet and add the solutions together
    for i in range(len(problem_symbols)):
        if problem_symbols[i] == "+":
            sum += addColumn([problem_number[i] for problem_number in problem_numbers])
        elif problem_symbols[i] == "*":
            sum += multiplyColumn([problem_number[i] for problem_number in problem_numbers])

    return sum


if __name__ == '__main__':
    start_time = time.time()
    with open(FILENAME) as f:
        fileContents = f.read().strip()
        problem_rows = fileContents.split("\n")
        # Replace occurrences of multiple spaces with a single one
        problem_rows = [" ".join(problem_row.split()) for problem_row in problem_rows]
        print(main(problem_rows))

    print(f"Time elapsed: {time.time() - start_time}s")
