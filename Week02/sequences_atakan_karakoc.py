my_list = [3,3,2,7,11,17,25,28,55,76,63,44,92,101]
my_tuple = (1,32,67,49,75)
my_set = {"Game of Thrones", "House of the Dragon", "TOP GUN"}
my_dict = {"Game of Thrones": 4, "House of the Dragon": 2, "TOP GUN": 1}

def remove_duplicates(my_list) -> list:
  return list(set(my_list))

def list_counts(my_list) -> dict:
  return {"i" : my_list.count(i) for i in my_list}

def reverse_dict(my_dict) -> dict:
  return {value: key for key, value in my_dict.items()}
