import time

from day4.adjacentTiles import getDirectionChecks

FILENAME = "input.txt"
PART = 1


def getIsAccessible(grid, x, y):
    """
    Get whether the forklift can access a roll of paper. A forklift can only access a position if there are fewer than
    four rolls of paper adjacent to the roll in all 8 directions.

    :param grid: the grid of paper rolls as a list of strings
    :param x: the row of the current tile
    :param y: the column of the current tile
    :return: True if the forklift can access the roll, False otherwise
    """
    adjacent_rolls = 0
    for has_roll in getDirectionChecks():
        adjacent_rolls += has_roll(grid, x, y)
        if adjacent_rolls >= 4:
            return False

    return True


def main(grid):
    """
    Compute the number of rolls of paper accessible to the forklift in a grid.

    :param grid: the grid of paper rolls as a list of strings
    :return: the number of accessible rolls of paper
    """
    num_accessible = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] != ".":
                num_accessible += getIsAccessible(grid, x, y)

    return num_accessible


if __name__ == "__main__":
    start_time = time.time()
    with open(FILENAME) as f:
        fileContents = f.read()
        sequence = fileContents.split("\n")
        print(main(sequence))

    print(f"Time elapsed: {time.time() - start_time}s")