my_list = [7, 8, 8, 9]
my_tuple = (7, 8, 9)
my_set = {7, 8, 9}
my_dict = {"name" : "rukiye"}

def remove_duplicates(my_list):
    temp_set = set(my_list)
    my_list.clear()
    my_list.extend(temp_set)
    return(my_list)


def list_counts(my_list):
    new_dict = {} 
    for item in my_list:
        if item in new_dict:
            new_dict[item] += 1
        else:
            new_dict[item] = 1  
    return(new_dict)

def reverse_dict(my_dict):
    reversed_dict = {}
    for key, value in my_dict.items():
        reversed_dict[value] = key
    return(reversed_dict)
