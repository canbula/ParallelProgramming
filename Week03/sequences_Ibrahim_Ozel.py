def remove_duplicates(seq: list) -> list:
    """
    Removes duplicate elements from a list while preserving order.
    """
    unique_items = []
    for item in seq:
        if item not in unique_items:
            unique_items.append(item)
    return unique_items


def list_counts(seq: list) -> dict:
    """
    Counts the number of occurrences of each item in a list.
    """
    counts = {}
    for item in seq:
        counts[item] = counts.get(item, 0) + 1
    return counts


def reverse_dict(d: dict) -> dict:
    """
    Reverses the keys and values of a dictionary.
    """
    reversed_dict = {}
    for key, value in d.items():
        reversed_dict[value] = key
    return reversed_dict
