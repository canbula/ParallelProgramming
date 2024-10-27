def remove_duplicates(seq: list) -> list:
    seen = []
    result = []
    for item in seq:
        if item not in seen:
            seen.append(item)
            result.append(item)
    return result

def list_counts(seq: list) -> dict:
    counts = {}
    for item in seq:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts

def reverse_dict(d: dict) -> dict:
    reversed_dict = {}
    for key, value in d.items():
        reversed_dict[value] = key
    return reversed_dict
