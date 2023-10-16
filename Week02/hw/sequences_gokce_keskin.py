my_list = [1, 3, 5, 7, 9]
my_tuple = (2, 4, 6, 8)
my_set = {11, 22, 33, 44}
my_dict = {"Blue": "Mavi", "Red": "Kirmizi", "Yellow": "Sari"}


def remove_duplicates(list_) -> list:
    return list(set(list_))


def list_counts(list_) -> dict:
    return {i: list_.count(i) for i in list_}


def reverse_dict(dict_) -> dict:
    return {value: key for key, value in dict_.items()}
