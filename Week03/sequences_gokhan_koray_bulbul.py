def remove_duplicates(seq: list) -> list:
    # returning list(set(seq)) would not preserve order
    unique_set = set()
    result = []
    for item in seq:
        if item not in unique_set:
            result.append(item)
            unique_set.add(item)
    return result
    
def list_counts(seq: list) -> dict:
    occurance_dict = dict.fromkeys(seq, 0)
    for item in seq:
        occurance_dict[item] += 1      
    return occurance_dict

def reverse_dict(d: dict) -> dict:
    reversed_dict = dict() 
    for key, value in d.items():
        reversed_dict[value] = key
    return reversed_dict
