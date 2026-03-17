def remove_duplicates(seq):
    result = []
    for item in seq:
        if item not in result:
            result.append(item)
    return result


def list_counts(seq):
    counts = {}
    for item in seq:
        if item not in counts:
            counts[item] = 0
        counts[item] += 1
    return counts


def reverse_dict(d):
    result = {}
    for key in d:
        result[d[key]] = key
    return result