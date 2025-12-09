import time

from day6.part1 import solveProblemByRows
from day6.part2 import solveProblemByDigits

FILENAME = "input.txt"
PART = 2
ROWS = 4 if FILENAME == "exampleInput.txt" else 5


def getProblemColumns(rows):
    """
    Split the problem sheet into a list of numeric tuples representing columns and a list of mathematical operators.

    :param rows: the problem sheet, comprised of a list of strings of spaced numbers
    :return: the columns for each problem
    """
    columns = []
    stripped_rows = [" ".join(row.split()) for row in rows]
    symbols = stripped_rows[-1].split()
    # Add a tuple containing each row in a column
    for i in range(len(symbols)):
        columns.append(tuple([int(row.split()[i]) for row in stripped_rows[:-1]]))

    return columns, symbols


def main(rows):
    """
    Solve a mathematical problem sheet by summing or multiplying columns and adding the results together.

    :param rows: a list of ROWS-1 strings of spaced numbers and a string of spaced mathematical operators
    :return: the total sum
    """
    columns, symbols = getProblemColumns(rows)
    if PART == 1:
        return solveProblemByRows(columns, symbols)
    elif PART == 2:
        return solveProblemByDigits(rows, columns, symbols)

    return sum


if __name__ == '__main__':
    start_time = time.time()
    with open(FILENAME) as f:
        fileContents = f.read()
        problem_rows = fileContents.split("\n")
        print(main(problem_rows))

    print(f"Time elapsed: {time.time() - start_time}s")
