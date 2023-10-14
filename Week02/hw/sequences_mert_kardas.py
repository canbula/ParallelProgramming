my_list = [1, 2, 3, 3, 4, 5, 5, 5, 6]
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
my_set = {1, 1, 1, 1, 1, 2, 2, 3, 3}
my_dict = {"age": 21, "isim": "Mert", "Şehir": "Manisa"}


def remove_duplicates(a_list: list[int]) -> list[int]:
    return list(set(a_list))


def list_counts(a_list: list[int]) -> dict[int, int]:
    a_dict = dict()
    for i in a_list:
        if a_dict.get(i):
            a_dict[i] += 1
        else:
            a_dict[i] = 1
    return a_dict


def reverse_dict(a_dict: dict) -> dict:
    dict_keys = a_dict.keys()
    dict_values = a_dict.values()
    return dict(zip(dict_values, dict_keys))
