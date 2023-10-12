my_list = [1,2,3,4]

my_tuple = (1,2,3,4)

my_set = {1,2,3,4}

my_dict = {"Name" : "Umut"}

def remove_dublicates(seq:list) -> list:
  return list(set(seq))

def list_counts(seq: list) -> dict:
    return {item: seq.count(item) for item in set(seq)}


def reverse_dict(d: dict) -> dict:
    return {value: key for key, value in d.items()}
  
  
