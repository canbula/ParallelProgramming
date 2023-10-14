my_list = [1, 2, 3, 3, 4]
my_tuple = (1, 2, 3, 3, 4)
my_set = {1, 2, 3, 3, 4}
my_dict = {1:1, 2:2, 3:3, 4:4}

def remove_duplicates(list_: list) -> list:
    return list(set(list_))

def list_counts(list_: list) -> dict:
    dict_ = dict.fromkeys(list_, 0)
    for item in list_:
        dict_[item] += 1
    return dict_

def reverse_dict(dict_: dict) -> dict:
    return {v: k for k, v in dict_.items()}
