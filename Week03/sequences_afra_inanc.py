def remove_duplicates(seq: list) -> list:
    result = []
    for element in seq:
        if element not in result:
            result += [element]
    return result


def list_counts(seq: list) -> dict:
    counts = {}
    for element in seq:
        if element not in counts:
            counts[element] = 0
        counts[element] += 1
    return counts


def reverse_dict(d: dict) -> dict:
    new_dict = {}
    for key in d:
        new_dict[d[key]] = key
    return new_dict
