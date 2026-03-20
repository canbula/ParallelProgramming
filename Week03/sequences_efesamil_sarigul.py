def remove_duplicates(sequence: list) -> list:
    new_list = []
    for item in sequence:
        if item not in new_list:
            new_list.append(item)
    return new_list

def list_counts(sequence: list) -> dict:
    counts = {}
    for item in sequence:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts

def reverse_dict(d: dict) -> dict:
    new_d = {}
    for k, v in d.items():
        new_d[v] = k 
    return new_d
