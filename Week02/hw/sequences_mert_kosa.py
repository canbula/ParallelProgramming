my_list= [1,2,3,4,5]
my_tuple= (1,2,3)
my_set= {1,2,3}
my_dict= {"one" : 1, "two" : 2, "three" : 3}

def remove_duplicates(my_list: list) -> list:
    return list(set(my_list))

def list_counts(my_list: list)-> dict:
    return {index: my_list.count(index) for index in set(my_list)}

def reverse_dict(my_dict: dict)-> dict:
    return{item: key for key, item in my_dict.items() }
