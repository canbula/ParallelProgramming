my_list = ["Bursa", 16, True, 50+10j]
my_tuple = (1,5,1)
my_set = {"CS", "Java" , 53}
my_dict = { 
            "name": "JunEscobar",
            "education": "Master Degree",
            "birth_year": 2001 
          }
def remove_duplicates(my_list):
    return list(set(my_list))

def list_counts(list):
    counts = {}
    for element in list:
      if element in counts:
          counts[element] += 1 
      else : 
          counts[element] = 1 
    return counts


def reverse_dict(dictionary):
    reverse_dict = {}
    for key, value in dictionary.items():
        reverse_dict[value] = key
    return reverse_dict
