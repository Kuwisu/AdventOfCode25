import time

from day4.adjacentTiles import getDirectionChecks

FILENAME = "input.txt"
PART = 2


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
    For part 1, compute the number of rolls of paper accessible to the forklift in a grid.
    For part 2, compute the number of rolls that can be removed by the Elves.

    :param grid: the grid of paper rolls as a list of strings, with a . corresponding to an empty space and an @ corresponding to a paper roll.
    :return: the number of accessible rolls of paper
    """
    num_accessible = 0
    num_removed = 0
    roll_locations = []
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == ".":
                continue

            roll_accessible = getIsAccessible(grid, x, y)
            if roll_accessible:
                num_accessible += 1
                if PART == 2:
                    # Replace the roll of paper in the grid with an empty space.
                    grid[x] = f"{grid[x][:y]}.{grid[x][y+1:]}"
                    num_removed += 1
            else:
                roll_locations.append((x, y))

    if PART == 1:
        return num_accessible

    # Repeatedly check the accessibility of rolls until all rolls are iterated through with no removal.
    removing_rolls = True
    while removing_rolls:
        removing_rolls = False
        for x, y in roll_locations:
            roll_accessible = getIsAccessible(grid, x, y)
            if roll_accessible:
                # Replace the roll of paper in the grid with an empty space.
                grid[x] = f"{grid[x][:y]}.{grid[x][y+1:]}"
                roll_locations.remove((x, y))
                num_removed += 1
                removing_rolls = True

    return num_removed


if __name__ == "__main__":
    start_time = time.time()
    with open(FILENAME) as f:
        fileContents = f.read()
        sequence = fileContents.split("\n")
        print(main(sequence))

    print(f"Time elapsed: {time.time() - start_time}s")