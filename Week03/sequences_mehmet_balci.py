def remove_duplicates(seq: list) -> list:
    seen = set()
    result = []
    for item in seq:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def list_counts(seq: list) -> dict:
    result = {}
    for item in seq:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result

def reverse_dict(d: dict) -> dict:
    reversed_d = {}
    for key, value in d.items():
        reversed_d[value] = key
    return reversed_d
