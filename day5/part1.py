from utils import parseIdRange


def isIngredientFresh(ingredient_id, ranges):
    """
    Check if an ingredient ID is fresh by checking to see if it falls within an ID range.

    :param ingredient_id: the numeric string ingredient ID
    :param ranges: a list of number ranges to compare the ID against
    :return: True if the ingredient falls into an ID range and is thus fresh, False otherwise
    """
    for id_range in ranges:
        start, end = parseIdRange(id_range)
        if start <= int(ingredient_id) <= end:
            return True

    return False


def countFreshIngredients(ranges, ids):
    """
    Count the number of fresh ingredients in a list of IDs.

    :param ranges: a list of string number ranges to compare the ID against
    :param ids: a list of numeric string IDs to check
    :return: the number of fresh ingredients
    """
    num_fresh = 0
    for ingredient_id in ids:
        num_fresh += isIngredientFresh(ingredient_id, ranges)

    return num_fresh