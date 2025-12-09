import re

def parseIdRange(id_range):
    """
    Parse a string corresponding to a range of integers into a start point and end point.

    :param id_range: a string following the format '<start>-<end>' where start and end are integers and end > start.
    :return: A tuple of integers (start, end)
    """
    pattern = re.compile(r"^(?P<start>[0-9]+)-(?P<end>[0-9]+)$")
    match = pattern.match(id_range)

    return int(match.group("start")), int(match.group("end"))