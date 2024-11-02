def remove_duplicates(seq: list) -> list:
    """
    This function removes duplicates from a list while preserving the original order.
    """
    unique_items = []
    for item in seq:
        if item not in unique_items:
            unique_items.append(item)
    return unique_items


def list_counts(seq: list) -> dict:
    """
    This function returns a dictionary with each item's occurrence count in the list.
    """
    frequency = {}
    for element in seq:
        if element in frequency:
            frequency[element] += 1
        else:
            frequency[element] = 1
    return frequency


def reverse_dict(d: dict) -> dict:
    """
    This function swaps keys and values in the given dictionary.
    """
    reversed_dict = {}
    for key, value in d.items():
        reversed_dict[value] = key
    return reversed_dict
