def remove_duplicates(seq: list) -> list:
    """
    Removes duplicate elements from a list and returns a new list with unique elements only.
    """
    return list(set(seq))


def list_counts(seq: list) -> dict:
    """
    Counts the occurrences of each element in a list and returns a dictionary with element frequencies.
    """
    result = dict.fromkeys(seq, 0)
    for i in seq:
        result[i] += 1
    return result


def reverse_dict(d: dict) -> dict:
    """
    Reverses the keys and values in a dictionary.
    """
    result = {}
    for i in d.items():
        result[i[1]] = i[0]
    return result
