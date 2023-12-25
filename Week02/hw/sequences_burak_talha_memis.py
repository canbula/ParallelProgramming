my_list = [1,2,3]

my_tuple = (1,2,3)

my_set = {1,2,3,4,5}

my_dict = {'first name' : 'Burak','second' : 'memis'}

def remove_duplicates(my_list):
  return list(set(my_list))

def list_counts(my_list):
    return {i: my_list.count(i) for i in my_list}

def reverse_dict(my_dict):
    return {v: k for k, v in my_dict.items()}
