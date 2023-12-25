def remove_duplicates(input_list):
    return list(set(input_list))

def list_counts(input_list):
    counts = {}
    for item in input_list:
        counts[item] = counts.get(item, 0) + 1
    return counts

def reverse_dict(input_dict):
    return {v: k for k, v in input_dict.items()}

# Creating the specified data structures
my_list = [1, 2, 3, 1, 2, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_set = {1, 2, 3, 4, 5}
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 2, 'e': 1}

