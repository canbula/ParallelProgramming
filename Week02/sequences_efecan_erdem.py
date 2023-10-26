my_list = [1,5,4,2,5,5,5,4,2,3]
my_tuple = (1,3,4,2)
my_set = {1,4,3,3,4,5,65,6,6,2}
my_dict = {"name" :"efecan",
           "surname": "erdem",
           "age": 22}

def remove_duplicates(list):
    ret_list = []

    for i in list:
        if i not in ret_list:
            ret_list.append(i)
    return ret_list

def list_counts(list):
    dict_ = {}

    for i in list:
        if i not in dict_:
            dict_[i] = 1
        else:
            dict_[i] +=  1
    return dict_

def reverse_dict(dict):
    reversed_dict = {}
    for i in dict:
        reversed_dict[dict[i]] = i
    return reverse_dict