

def remove_duplicates(seq:list) -> list:
    '''
    This function removes duplicates from a list
    Args:
        seq (list): Input list with potential duplicates
    
    Returns:
        list (list): List with duplicates removed
    '''
    return list(set(seq))

def list_counts(seq:list) -> dict:
    '''
    This function counts the occurences of each element in a list

    Args:
        seq (list): Input list to count occurences of each element
    
    Returns:
        dict (dict): Dictionary with elements as keys and occurences as values

    '''
    count={}

    for i in seq:
        count[i]=seq.count(i)
    
    return count
    #{i: seq.count(i) for i in seq}

def reverse_dict(d:dict) -> dict:
    '''
    This function reverses the keys and values of a dictionary

    Args:
        d (dict): Input dictionary to reverse keys and values

    Returns:
        dict (dict): Dictionary with keys and values reversed
    '''

    reversed={}

    for key, value in d.items():
        reversed[value] = key

    return reversed
    #return {v: k for k, v in d.items()}