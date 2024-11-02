def remove_duplicates(seq: list) -> list:
    """
    This function removes duplicates from a list.
    """
    return list(set(seq))


def list_counts(seq: list) -> dict:
    """
    This function counts the number of occurrences of each item in a list.
    """
    counts = {}
    for item in seq:
        counts[item] = counts.get(item, 0) + 1
    return counts


def reverse_dict(d: dict) -> dict:
    """
    This function reverses the keys and values of a dictionary.
    """
    return {value: key for key, value in d.items()}
