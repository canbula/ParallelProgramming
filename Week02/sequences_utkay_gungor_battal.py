my_list = [7, 12, 5, 9, 154, 7]
my_tuple = (2, 7, 30, 24, 0)
my_set = {13, 9, "Kocaeli", 86}
my_dict = {"name" : "Utkay", "name" : "Eren", "name" : "Beyza"}

def remove_dublicates(list):
  new_list = []
  for element in list: 
    if element not in new_list:
      new_list.append(element)

return new_list


def list_counts(list):
  counts = {}
  for element in list:
    if element in counts:
      counts[element] += 1
    else:
      counts[element] = 1 

return counts


def reverse_dict(dictionary):
  reverse_dict = {}
  for key, value in dictionary.items():
    reverse_dict[value] = key 

return reverse_dict


