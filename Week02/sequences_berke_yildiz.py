my_list = ["A", "B", "C", "D", "A", "B"]
my_tuple = (1,4,10,3,6,9,2)
my_set = {"A", 2, "B", 3, "C"}
my_dict = {"A" : 3, "B" : 2, "C" : 1}

def remove_duplicates(my_list):
    return list(set(my_list))

def list_counts(my_list):
    the_list = list(my_list)
    the_dict = {}

    for item in the_list:
        occurance = the_list.count(item)
        the_dict[item] = occurance
    return the_dict

def reverse_dict(my_dict):
    the_dict = dict(my_dict)
    new_dict = {}
    for item in the_dict:
        new_dict[the_dict[item]] = item 
    return new_dict
