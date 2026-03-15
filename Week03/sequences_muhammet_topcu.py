from collections import Counter

def remove_duplicates(lst):
    return list(dict.fromkeys(lst))

def list_counts(lst):
    return dict(Counter(lst))

def reverse_dict(d):
    result = {}
    for k, v in d.items():
        result[v] = result.get(v, 0) + k
    return result
