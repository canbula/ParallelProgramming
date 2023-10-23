my_list = [1, "Wow", 2.1]
my_tuple = (1, "Wow", 2.1)
my_set = {1, "Wow", 2.1}
my_dict = {1:1, "Wow":"Wow", 2.1: 2.1}

def remove_duplicates(my_list):
  return list(set(my_list))

def list_counts(my_list):
  return {item: my_list.count(item) for item in my_list}

def reverse_dict(my_dict):
  return {value: key for key, value in my_dict.items()}
