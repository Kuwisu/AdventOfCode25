from day6.utils import addColumn, multiplyColumn


def padRows(rows):
    """
    Pad the length of strings to keep the same amount of digits between rows

    :param rows: a list of strings
    """
    max_length = max([len(row) for row in rows[:-1]])
    for i in range(len(rows[:-1])):
        rows[i] = rows[i].ljust(max_length - 1) + " "


def solveProblemByDigits(rows, columns, symbols):
    """
    Solve a problem sheet by adding or multiplying a column of numbers, determining the numbers from the rightmost to
    the leftmost digit and choosing the operation according to the corresponding symbol.


    :param rows: a list of strings of spaced numbers and a string of spaced mathematical operators
    :param columns: a list of integer tuples
    :param symbols: a list of mathematical operators with the same shape as columns
    :return: the sum of all solved columns.
    """
    out = 0
    i = 0
    padRows(rows)
    for j in range(len(symbols)):
        # Get the number of digits in the longest number in the column
        digits = len(str(max(columns[j])))
        column = []
        for k in range(digits):
            # Concatenate the digits (k+1) in each row and add to the list as an integer
            column.append(int("".join([row[i + k] for row in rows[:-1]])))

        i += digits + 1
        if symbols[j] == "+":
            out += addColumn(column)
        elif symbols[j] == "*":
            out += multiplyColumn(column)

    return out
