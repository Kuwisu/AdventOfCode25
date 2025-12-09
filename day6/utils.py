
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