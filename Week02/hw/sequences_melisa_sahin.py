my_list = [1,2,2,3,3,3,4,4,4,4,5,5,6]
my_tuple = (7,8,9,10)
my_set = {"Java", "Python", "PHP", "C#"}
my_dict = {"Name" : "Melisa", "Surname" : "Sahin" , "Department" : "Comp_Eng" , "Number" : 200315046}


def remove_duplicates(my_list):
    new_list = []
    for i in my_list:
        if i not in new_list:
            new_list.append(i)
    return new_list  

             
def list_counts(my_list):
    return {i : my_list.count(i) for i in my_list} 
     

def reverse_dict(my_dict):
    reversed_dict = {}
    for key,value in my_dict.items():
        reversed_dict[value] = key
    return reversed_dict    
