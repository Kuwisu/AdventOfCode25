def moveBeam(rows, x, y):
    """
    Recursively move the beam downward until it reaches the final point, counting 1 each time the beam splits.

    :param rows: a list of strings representing the tachyon manifold
    :param x: the current x coordinate of the beam
    :param y: the current y coordinate of the beam
    :return: a count of the number of times the beam has split after this call
    """
    # Skip if the beam has been split into an occupied space or if the bottom has been reached.
    if rows[x][y] == "|" or x == len(rows) - 1:
        return 0

    # Update the current tile and move the beam downwards
    rows[x] = f"{rows[x][:y]}|{rows[x][y+1:]}"
    if rows[x+1][y] == ".":
        return 0 + moveBeam(rows, x+1, y)
    elif rows[x+1][y] == "^":
        return 1 + moveBeam(rows, x+1, y-1) + moveBeam(rows, x+1, y+1)

    return 0
