def remove_duplicates(seq: list) -> list:
    """
    This function removes duplicates from a list.
    """ 
    unique_items = []
    for item in seq:
        if item not in unique_items:
            unique_items.append(item)
    return unique_items

def list_counts(seq: list) -> dict:
    """
    This function counts the number of 
    occurrences of each item in a list.
    """
    counts = {}
    for item in seq:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts

def reverse_dict(d: dict) -> dict:
    """
    This function reverses the keys
    and values of a dictionary
    """
    reversed_dict = {}
    for key, value in d.items():
        reversed_dict[value] = key
    return reversed_dict    
