def remove_duplicates(seq: list) -> list:
    return [item for i, item in enumerate(seq) if item not in seq[:i]]

def list_counts(seq: list) -> dict:
    counts = {}
    for item in seq:
        counts[item] = counts.get(item, 0) + 1
    return counts

def reverse_dict(d: dict) -> dict:
    reversed_dict = {}
    for k in d:
        reversed_dict[d[k]] = k
    return reversed_dict
