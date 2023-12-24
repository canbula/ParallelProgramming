my_list = [1,2,3]

my_tuple = (1,2,3)

my_set = {1,3,5}

my_dict = {"name" : "Akif",
           "age" : "23"}

def remove_duplicates (input_list):
 return list(set(input_list))

def list_counts(input_list):
  counted_dict = {}
  for i in input_list:
    if i in counted_dict:
      counted_dict[i] += 1
    else:
      counted_dict[i] = 1
  return counted_dict

def reverse_dict(input_dict):
  reversed_dict = {}
  for key, value in input_dict.items():
    reversed_dict[value] = key
  return reversed_dict
