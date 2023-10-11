my_list = [0, 2, 4, 6]
my_tuple = (1, 1, 3, 5, 7)
my_set = (1, 3, 5, 7)
my_dict = {"name" : "zehra", "age" : 20, "job" : "computerEngineer"}

def remove_duplicates(input_list):
  last_list = list[]
  for i in input_list:
    last_list.append(i)
  return last_list

def list_counts(input_list):
    count_dict = {}
    for i in input_list:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    return count_dict

def reverse_dict(input_dict):
    reversed_dict = {value: key for key, value in input_dict.items()}
    return reversed_dict
  
