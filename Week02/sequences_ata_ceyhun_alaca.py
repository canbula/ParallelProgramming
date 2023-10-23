my_list = [3, 6.7, 3, 8, 8, 55, 5, 34, 133, 345, 3456, 2, 5, 43, 2, 2, 1.2]
my_tuple = (3, 12, 65, 43, 12)
my_set = {"Formula1", "Formula2", "Formula3"}
my_dict = {"Day One": 1,"Day Two": 2, "Day Three": 3}


def remove_duplicates(my_list) -> list:
  return list(set(my_list))

def list_counts(my_list) -> dict:
  return {elemnt_count: my_list.count(e) for e in set(my_list)}

def reverse_dict(my_dict) -> dict:
  return {value: key for key, value in my_dict.items()}
