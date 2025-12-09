from utils import parseIdRange


def mergeIdRanges(id_ranges):
    """
    Iterate through a list of ID ranges and merge any pairs of ranges that overlap with each other.

    :param id_ranges: a list of integer ID ranges in the form (start, end)
    """
    for i in range(len(id_ranges)):
        for j in range(i + 1, len(id_ranges)):
            # Identify overlapping ranges and merge the smallest and largest dimensions
            if (
                    id_ranges[i][1] >= id_ranges[j][0] >= id_ranges[i][0]
                    or id_ranges[i][0] <= id_ranges[j][1] <= id_ranges[i][1]
            ):
                id_ranges.append((
                    min(id_ranges[i][0], id_ranges[j][0]),
                    max(id_ranges[i][1], id_ranges[j][1])
                ))

                # Remove redundant ranges and call function again to identify new overlap
                id_ranges.remove(id_ranges[i])
                id_ranges.remove(id_ranges[j - 1])
                mergeIdRanges(id_ranges)


def countFreshIds(id_ranges):
    """
    Count the number of IDs in a list of ID ranges while accounting for overlapping ranges.

    :param id_ranges: a list of string ID ranges in the form "<start>-<end>"
    :return: the number of IDs encompassed in the ranges
    """
    count = 0
    output_ranges = []
    for id_range in id_ranges:
        output_ranges.append(parseIdRange(id_range))
        mergeIdRanges(output_ranges)

    for id_range in output_ranges:
        count += id_range[1] - id_range[0] + 1

    return count
