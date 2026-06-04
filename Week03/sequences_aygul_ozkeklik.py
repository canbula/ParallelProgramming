def remove_duplicates(my_list):
    result = []
    for item in my_list:
        if item not in result:
            result.append(item)
    return result


def list_counts(my_list):
    counts = {}
    for item in my_list:
        counts[item] = counts.get(item, 0) + 1
    return counts


def reverse_dict(d):
    reversed_d = {}
    for k, v in d.items():
        reversed_d[v] = k
    return reversed_d
