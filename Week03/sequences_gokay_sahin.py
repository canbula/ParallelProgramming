def remove_duplicates(seq: list) -> list:
    list = []
    for i in seq:
        if i not in list:
            list.append(i)
    return list

def list_counts(seq: list) -> dict:
    dict = {}
    for i in seq:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    return dict

def reverse_dict(d: dict) -> dict:
    reversed_d = {}
    for key in d:
        value = d[key]
        reversed_d[value] = key
    return reversed_d
