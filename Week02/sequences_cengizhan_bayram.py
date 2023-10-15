my_list = [1, 2, 3, 3, 4, 5, 5, 5, 6, 6, 6, 7]
my_tuple = (1, 2, 3, 4, 5, 6)
my_set = {1, 1, 1, 1, 1, 2, 2, 3, 4, 5, 6}
my_dict = {"nickname": "metalsnake ", "name": "Cengizhan", "age": 22}


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


def reverse_dict(my_dict):
    rev_dictionary = dict()
    for key, value in my_dict.items():
        rev_dictionary[value] = key
    return(rev_dictionary)
