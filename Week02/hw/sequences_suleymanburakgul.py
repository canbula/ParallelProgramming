my_list = [2, 7, 1, 4, 4, 43, 12, 78, 256, 2, 5, 23, 2]
my_tuple = (1, 24, 32, 76, 19)
my_set = {"Kebabos", "Game", "Developer"}
my_dict = {"Balls and Coins": 1,"Grunenberg": 2, "Up to Gods": 3}


def remove_duplicates(my_list) -> list:
  return list(set(my_list))

def list_counts(my_list) -> dict:
  return {element_count: my_list.count(element_count) for element_count in set(my_list)}

def reverse_dict(my_dict) -> dict:
  return {value: key for key, value in my_dict.items()}
