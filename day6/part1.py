from day6.utils import addColumn, multiplyColumn


def solveProblemByRows(columns, symbols):
    """
    Solve a problem sheet by adding or multiplying a column of numbers row by row, choosing the operation according to the corresponding symbol.

    :param columns: a list of integer tuples
    :param symbols: a list of mathematical operators with the same shape as columns
    :return: the sum of all solved columns.
    """
    out = 0
    # Solve each problem in the sheet and add the solutions together
    for i in range(len(symbols)):
        if symbols[i] == "+":
            out += addColumn(columns[i])
        elif symbols[i] == "*":
            out += multiplyColumn(columns[i])

    return out