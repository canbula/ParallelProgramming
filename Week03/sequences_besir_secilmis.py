def remove_duplicates(seq : list) -> list:
    return list(set(seq))

def list_counts(seq:list) -> dict:
    L = {}
    for i in seq:
        if i in L:
            L[i] += 1
        else:
            L[i] = 1
    return L

def reverse_dict(d : dict) -> dict:
    rd = {}
    for i, h in d.items():
        rd[h] = i
    return rd
