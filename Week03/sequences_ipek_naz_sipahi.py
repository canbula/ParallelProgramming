def remove_duplicates(seq: list) -> list:
    seen = set()
    result = []
    for item in seq:
        if item not in seen:
            seen.add(item)
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
    reversed_dict = {v: k for k, v in d.items()} # Reverse the keys and values using dictionary comprehension
    return reversed_dict
