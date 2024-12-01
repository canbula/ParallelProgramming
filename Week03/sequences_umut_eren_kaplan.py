def remove_duplicates(seq: list) -> list:
    """
    This function removes duplicates from a list.
    """
    return list(set(seq))

def list_counts(seq: list) -> dict:
    """
    This function counts the number of occurrences of each item in a list.
    """
    counted = {}
    for item in seq:
        counted[item] = seq.count(item)
    return counted

def reverse_dict(d: dict) -> dict:
    """
    This function reverses the keys
    and values of a dictionary.
    """
    return {v: k for k, v in d.items()}
