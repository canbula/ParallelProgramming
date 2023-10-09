my_list = [1,2,3,4,5]
my_tuple = (3,6,9,9,8,7,4,5,4)
my_set = {4,7,8,7,8,9}
my_dict = {"name" : "Beyza",
           "surname" :"Sungar",
           "city" : "Eskişehir",
           "age" : 21}

def remove_duplicates(my_list)
   return list(set(my_list))

def list_counts(my_list)
   counts = {}
    for item in input_list:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts

def reverse_key(dictionary):
    return {value: key for key, value in dictionary.items()}
