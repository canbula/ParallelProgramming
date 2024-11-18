def remove_duplicates(seq: list) -> list:
    """
    This function removes duplicates from a list.
    """
    return list(dict.fromkeys(seq))  # Using dict.fromkeys to remove duplicates while maintaining order.

def list_counts(seq: list) -> dict:
    """
    This function counts the number of occurrences of each item in a list.
    """
    return {item: seq.count(item) for item in set(seq)}  # Counts occurrences by iterating over unique items in the list.

def reverse_dict(d: dict) -> dict:
    """
    This function reverses the keys and values of a dictionary.
    """
    return {v: k for k, v in d.items()}  # Swaps keys and values to reverse the dictionary.
