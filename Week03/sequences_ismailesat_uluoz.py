def remove_duplicates(seq: list) -> list:
    new_list = []
    for item in seq:
        if item not in new_list:
            new_list.append(item)
    return new_list


def list_counts(seq: list) -> dict:
    counts = {}
    for item in seq:
        if item not in counts:
            counts[item] = 1
        else:
            counts[item] = counts[item] + 1
    return counts


def reverse_dict(d: dict) -> dict:
    new_dict = {}
    for key in d:
        new_dict[d[key]] = key
    return new_dict
