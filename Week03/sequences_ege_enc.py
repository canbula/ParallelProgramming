def remove_duplicates(seq : list) -> list:
    return list(set(seq))

def list_counts(seq:list) -> dict:
    d = {}
    for i in seq:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d

def reverse_dict(d : dict) -> dict:
    nd = {}
    for i, h in d.items():
        nd[h] = i
    return nd
