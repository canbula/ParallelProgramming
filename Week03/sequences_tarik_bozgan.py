def remove_duplicates(seq):
    result = []
    for item in seq:
        if item not in result:
            result.append(item)
    return result


def list_counts(seq):
    counts = {}
    for item in seq:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts


def reverse_dict(d):
    reversed_dict = {}
    for key, value in d.items():
        reversed_dict[value] = key
    return reversed_dict