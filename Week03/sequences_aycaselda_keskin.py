def remove_duplicates(seq: list) -> list:

    return list(set(seq))

def list_counts(seq: list) -> dict:

    counts_dict = {} 
    
    for item in seq:
        counts_dict[item] = seq.count(item) 
        
    return counts_dict

def reverse_dict(d: dict) -> dict:

    reversed_d = {} 
    for k, v in d.items():
        
      reversed_d[v] = k 
        
    return reversed_d
