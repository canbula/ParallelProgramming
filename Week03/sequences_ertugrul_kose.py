def remove_duplicates(seq: list) -> list:
    """
    This function removes duplicates from a list.
    """ 
    unique = []
    for x in seq:
        if x not in unique:
            unique.append(x)
    return unique


def list_counts(seq: list) -> dict:
    """
    This function counts the number of 
    occurrences of each item in a list.
    """
    result = {}
    for x in seq:
        if x in result:
            result[x] += 1
        else:
            result[x] = 1
    return result


def reverse_dict(d: dict) -> dict:
    """
    This function reverses the keys
    and values of a dictionary
    """
    rev = {}
    for k, v in d.items():
        rev[v] = k
    return rev
