
def remove_duplicates(seq: list) -> list:
    """
    This function removes duplicates from a list.
    """
    return list(set(seq))
  
  
  
  
def list_counts(seq: list) -> dict:
    """
    This function counts the number of occurrences
    of each item in a list more efficiently.
    """
    return {i: seq.count(i) for i in set(seq)}



def reverse_dict(d: dict) -> dict:
    """
    This function reverses the keys
    and values of a dictionary.
    """
    return {y: k for k, y in d.items()}
