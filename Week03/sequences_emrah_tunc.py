def remove_duplicates(seq: list) -> list:
    new_list = []  
    
    for value in seq:       
        if value not in new_list:
            new_list.append(value)
            
    return new_list

def list_counts(seq: list) -> dict:
    counter = {}    
    for element in seq:
        if element in counter:
           counter[element] = counter[element] + 1
        
        else:
           counter[element] = 1
            
    return counter

def reverse_dict(d: dict) -> dict:
    reversed_d = {}
    
        for key, value in d.items():
            reversed_d[value] = key
        
    return reversed_d
