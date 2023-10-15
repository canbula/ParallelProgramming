my_list = [1, 2, 2, 3, 4, 4, 4]


my_tuple = (1, 2, 3, 4, 5)


my_set = {1, 2, 2, 3, 4, 4, 5}


my_dict = {'Adekugbe': 5, 'Aboubakar': 3, 'Tadic': 7}


def remove_duplicates(input_list):
    return list(set(input_list))


def list_counts(input_list):
    counts = {}
    for item in input_list:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts


def reverse_dict(input_dict):
    reversed_dict = {value: key for key, value in input_dict.items()}
    return reversed_dict


unique_list = remove_duplicates(my_list)
print("Unique List:", unique_list)

counts = list_counts(my_list)
print("List Counts:", counts)

reversed_dict = reverse_dict(my_dict)
print("Reversed Dictionary:", reversed_dict)
