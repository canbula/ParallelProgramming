def remove_duplicates(seq: list) -> list:
    first = set()  
    second = []
    
    for item in seq:
        if item not in first:
            second.append(item)
            first.add(item)
    
    return second

def list_counts(seq: list) -> dict:
    counts = {}
    
    for item in seq:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    
    return counts

def reverse_dict(d: dict) -> dict:
    reversed_dict = {v: k for k, v in d.items()}
    return reversed_dict
