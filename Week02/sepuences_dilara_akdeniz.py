my_list = [1, 2, 3, 4, 5]
my_tuple = (6, 7, 8, 9)
my_set = {a, b, c, d}
my_dict = {"name" : "dilara", "surname" : "akdeniz", "number" : "200315067", "gender" : "female"}

def remove_duplicates(my_list):
  return list(set(my_list))

def list_count(my_list):
  return {i: my_list.count(i) for i in my_list}

def reverse_dict(my_dict):
  return {v : k for k, v in my_dict.items()}
