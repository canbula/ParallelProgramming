my_list = [1, 2, 2, 3, 3]
my_tuple = (1, 2, 3, 4)
my_set = {1, 2, 3}
my_dict = {
           'Test1': 123456,
           'Test2': 789012, 
           'Test3': 345678
          }

def remove_duplicates(my_list):
    my_set = set(my_list)
    my_list = list(my_set)
    return my_list

print(remove_duplicates(my_list))

def list_counts(list):
    counts_dictionary = {}

    for item in list:
        if item in counts_dictionary :
            counts_dictionary [item] += 1
        else:
            counts_dictionary [item] = 1
    return counts_dictionary 

print(list_counts(my_list))

def reverse_dictionary(dict):
    reversed_dictionary = {}

    for key, value in dict.items():
        reversed_dictionary[value] = key

    return reversed_dictionary

print(reverse_dictionary(my_dict))
