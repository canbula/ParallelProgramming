my_list = [1, 2, 3, 4, 5, 4, 3, 2, 1]
my_tuple = (1, 2, 3, 4, 5)
my_set = {1, 2, 3, 4, 5}
my_dict = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}

def remove_duplicates(some_list):
    return list(set(some_list))

def list_counts(some_list):
    return {i: some_list.count(i) for i in some_list}

def reverse_dict(some_dict):
    return {v: k for k, v in some_dict.items()}
