def remove_duplicates(input_list):
    seen = set()
    result = []
    for item in input_list:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result


def list_counts(input_list):
    counts = {}
    for item in input_list:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts


def reverse_dict(input_dict):
    reversed_dict = {}
    for key, value in input_dict.items():
        reversed_dict[value] = key
    return reversed_dict
