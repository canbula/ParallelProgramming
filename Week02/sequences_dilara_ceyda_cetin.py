my_list = [10, 11, [12,'Jack',13], "Python"]
my_tuple = (5, 6, 7)
my_set = {10, 11, (5,6,7), 12, 13}
my_dict = {"Ada": 88, "Kübra": 100, "Sena": 5}

def remove_duplicates(input_list):
    return list(set(input_list)

def list_counts(input_list):
  counter = {}
    for i in input_list:
      if i in counter:
        counter[i] +=1
      else:
        counter[i] = 1
    return counter

def reverse_dict(input_dict):
  reversed_dict{}
    for key, value in input_dict.items():
      reversed_dict[value] = key

    return reversed_dict
