def remove_duplicates(seq: list) -> list:
    new_list = []
    for i in seq:              
        if i not in new_list:  
            new_list.append(i) 
    return new_list


def list_counts(seq: list) -> dict:
    result = {}             
    for i in seq:           
        if i in result:     
            result[i] = result[i] + 1
        else:               
            result[i] = 1
    return result           


def reverse_dict(d: dict) -> dict:
    reversed_d = {}
    for k in d:
        value = d[k]
        reversed_d[value] = k
    return reversed_d
