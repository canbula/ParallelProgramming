def remove_duplicates(seq):
    unique_items = []
    for item in seq:
        if item not in unique_items:
            unique_items.append(item)
    return unique_items

def list_counts(seq):
    item_counts = {}
    for item in seq:
        if item in item_counts:
            item_counts[item] += 1
        else:
            item_counts[item] = 1
    return item_counts

def reverse_dict(d):
    reversed_dict = {}
    for key, value in d.items():
        reversed_dict[value] = key
    return reversed_dict

# Example Data
my_list = [2, 6, 8]
my_tuple = (4, 6, 9)
my_set = {3, 4, 5}
my_dict = {1: 4, 5: 7, 7: 5}

#Sample transactions
unique_list = remove_duplicates(my_list)
item_counts_dict = list_counts(my_list)
reversed_dict = reverse_dict(my_dict)

