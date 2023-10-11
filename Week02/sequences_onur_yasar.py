my_list = [1,2,3]
my_tuple = (1,2,3)
my_set = {1,2,3}
my_dict = {
    'Test': 123,
    'Test2': 1234,
}


def remove_duplicates(list_):
    new_set = set()
    for item in list_:
        new_set.add(item)
    return list(new_set)

def list_counts(list):
    counts_dictionary = {}
    for item in list:
        if counts_dictionary.get(item):
            counts_dictionary[item] = counts_dictionary[item] + 1
        else:
            counts_dictionary[item] = 1
    return counts_dictionary

def reverse_dict(dict):
    reversed_dict = {}
    dict_keys = list(dict.keys())
    for key in dict_keys:
        reversed_dict[dict[key]] = key
    
    return reversed_dict