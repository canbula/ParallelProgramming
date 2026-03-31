def remove_duplicates(seq: list) -> list:
    unique_items = []

    for item in seq:
        if item not in unique_items:
            unique_items.append(item)

    return unique_items


def list_counts(seq: list) -> dict:
    counts = {}

    for item in seq:
        counts[item] = counts.get(item, 0) + 1

    return counts


def reverse_dict(d: dict) -> dict:
    reversed_dictionary = {}

    for key, value in d.items():
        reversed_dictionary[value] = key

    return reversed_dictionary