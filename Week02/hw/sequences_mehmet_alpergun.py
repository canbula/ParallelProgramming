
my_list = [1,3,5]
my_tuple = (3,6,9)
my_set = {2,4,6}
my_dict = {1: 3, 5: 7, 8: 6}

def remove_duplicates(seq: list) -> list:
 return list(set(seq))

def list_counts(seq: list) -> dict:
  return{item: seq.count(item) for item in set(seq)}

def reverse_dict(d: dict) -> dict:
  return {value: key for key, value in d.items()}
