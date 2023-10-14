my_list = [1,4,6,2,3,7,9,8,0]
my_tuple = (5, 6, 6, 7, 8, 8, 9)
my_set = {4, 5, 6, 7, 8}
my_dict = {"name": "Ferhat", "surname": "Kurkcuoglu", "age": 21}

def remove_duplicates(my_list):
    return list(set(my_list))


def list_counts(my_list):
    count_dict = {}
    for element in my_list:
        if element in count_dict:
            count_dict[element] += 1
        else:
            count_dict[element] = 1
    return count_dict


def reverse_dict(my_dict):
    reversed_dictionary = dict()
    for key, value in my_dict.items():
        reversed_dictionary[value] = key
    print(reversed_dictionary)
