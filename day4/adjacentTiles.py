def topLeftOccupied(grid, x, y):
    return True if y > 0 and x > 0 and grid[x - 1][y - 1] == "@" else False

def topOccupied(grid, x, y):
    return True if x > 0 and grid[x - 1][y] == "@" else False

def leftOccupied(grid, x, y):
    return True if y > 0 and grid[x][y - 1] == "@" else False

def topRightOccupied(grid, x, y):
    return True if x > 0 and y < len(grid[0]) - 1 and grid[x - 1][y + 1] == "@" else False

def bottomLeftOccupied(grid, x, y):
    return True if y > 0 and x < len(grid[0]) - 1 and grid[x + 1][y - 1] == "@" else False

def rightOccupied(grid, x, y):
    return True if y < len(grid[0]) - 1 and grid[x][y + 1] == "@" else False

def bottomOccupied(grid, x, y):
    return True if x < len(grid[0]) - 1 and grid[x + 1][y] == "@" else False

def bottomRightOccupied(grid, x, y):
    return True if x < len(grid[0]) - 1 and y < len(grid[0]) - 1 and grid[x + 1][y + 1] == "@" else False

def getDirectionChecks():
    return [topLeftOccupied, topOccupied, leftOccupied, topRightOccupied, bottomLeftOccupied,
            rightOccupied, bottomOccupied, bottomRightOccupied]
