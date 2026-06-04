def remove_duplicates(my_list):
    return list(dict.fromkeys(my_list))


def list_counts(my_list):
    counts = {}
    for item in my_list:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts


def reverse_dict(my_dict):
    reversed_results = {}
    for key, value in my_dict.items():
        reversed_results[value] = key
    return reversed_results
