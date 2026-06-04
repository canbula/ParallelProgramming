def remove_duplicates(seq):
    unique_values = []
    seen = set()

    for item in seq:
        if item not in seen:
            unique_values.append(item)
            seen.add(item)

    return unique_values


def list_counts(seq):
    counts = {}

    for item in seq:
        counts[item] = counts.get(item, 0) + 1

    return counts


def reverse_dict(d):
    flipped = {}

    for key in d:
        value = d[key]
        flipped[value] = key

    return flipped
