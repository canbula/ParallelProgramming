my_list = [1,2,3,4]

my_tuple = ("str" , 6 , 1.0)

my_set = {1,"str", True}

my_dic = {
    1 : "first",
    2 : "second",
    3 : "third" 
}

def remove_duplicates(received_list : list) -> list:
    return list(set(received_list))

def list_counts(list: list) -> dict:
    dic = {}
    for i in range(len(list)):
        dic[i] = list[i]
    return dic

def reverse_dict(dic : dict) -> dict:
    new_dic = {}
    for key , value in dic.items():
        new_dic[value] = key
    return new_dic
