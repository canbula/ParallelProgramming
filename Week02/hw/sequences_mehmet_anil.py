my_list = [35, 45, 16, 34, 34]

my_tuple = ("leo", "ronaldo","drogba","drogba")

my_set = ("banana","true","1")

my_dict = {
    "name": "mehmet",
    "nickname": "kralex",
    "dateOfBirth": "2000"
}


def remove_dublicates_list (my_tuple):

    unique_list = []

    for item in my_tuple:
        if item not in unique_list:
            unique_list.append(item)

    return unique_list

result = remove_dublicates_list(my_tuple)
print(result)





my_input_list = [4, 4, 4, 4, 5, 5, 6, 7, 7]

def list_counts(my_input_list):
    counts = {}  # Create an empty dictionary to store the counts

    for item in my_input_list:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1

    return counts

result_1 = list_counts(my_input_list)
print(result_1)

def reverse_dict(my_dict):
    reversed_dict = {value: key for key, value in my_dict.items()}
    return reversed_dict

result_2 = reverse_dict(my_dict)
print(result_2)
