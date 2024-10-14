def remove_duplicates(seq: list) -> list:
    """
    This function removes duplicates from a list.
    """
    seq = list(set(seq))
    
    return seq

def list_count(seq: list) -> dict:
    """
    This functioncounts the number of occurences of each item in a list.
    """
    count_dict = {}
    
    for i in seq:
        if i in count_dict :
            count_dict[i] += 1
        else:
            count_dict[i] = 1

    return count_dict

def reverse_dict(d: dict) -> dict:
    """
    This function reverses the keys and values of a dictionary.
    """
    reversed_dict = {}
    for key, value in d.items():
        reversed_dict[value] = key
        
    return reversed_dict
   

# Testler
print(remove_duplicates([1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 9, 9, 9, 9]))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list_count([1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 9, 9, 9, 9])  )   # {1: 1, 2: 1, 3: 1, 4: 1, 5: 3, 6: 1, 7: 1, 8: 1, 9: 5}

print(reverse_dict({'a': 1, 'b': 2, 'c': 3, 'd': 2}))  # {1: 'a', 2: 'd', 3: 'c'}
