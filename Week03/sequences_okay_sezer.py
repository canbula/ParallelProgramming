def remove_duplicates(seq: list) -> list:
    list = []
    for item in seq:
        if item not in list:
            list.append(item)
    return list

def list_counts(seq: list) -> dict:
    dict = {}
    for item in seq:
        if item in dict:
            dict[item] += 1
        else:
            dict[item] = 1
    return dict

def reverse_dict(d: dict) -> dict:
    reversed_dict = {}
    for key, value in d.items():
        reversed_dict[value] = key
    return reversed_dict
