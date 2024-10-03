def remove_duplicates(seq: list) -> list:
    if not seq:  # Handle empty input
        return []
    
    uniq_list = [seq[0]] 
    index = 0
    for number in seq:
        if not uniq_list[index] == number:
            uniq_list.append(number)
            index+=1    
    return uniq_list

def list_counts(seq: list) -> dict:
    my_dict = {}
    for number in seq:
        if number in my_dict:
            my_dict[number] += 1
        else:
            my_dict[number] = 1
    return my_dict

def reverse_dict(d: dict) -> dict:
    reversed_dict = {}
    for k,v in d.items():
        reversed_dict[v] = k
    return reversed_dict
