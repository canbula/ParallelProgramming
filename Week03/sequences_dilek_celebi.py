def remove_duplicates(lst):
    unique_items = []
    for item in lst:
        if item not in unique_items:
            unique_items.append(item)
    return unique_items


def list_counts(lst):
    frequency_dict = {}
    for item in lst:
        if item in frequency_dict:
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1
    return frequency_dict


def reverse_dict(d):
    swapped_dict = {}
    for key, value in d.items():
        swapped_dict[value] = key
    return swapped_dict
