my_list = [1,2,3,4,5,5,5]

my_tuple = (1,2,3,False)

my_set = {1,2,3,4,5}

my_dict = {"isim" : "Batuhan",
           "yaş" : "22"}

def remove_duplicates (input_list):
 return list(set(input_list))


def list_counts(input_list):
  counter_dict = {}

  for item in input_list:
    if item in counter_dict:
      counter_dict[item] += 1
    else:
      counter_dict[item] = 1

  return counter_dict



def reverse_dict(input_dict):
  reversed_dict = {}

  for key, value in input_dict.items():
    reversed_dict[value] = key

  return reversed_dict
