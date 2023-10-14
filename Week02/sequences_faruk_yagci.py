my_list = [2,0,0,3,1,5,0,6,8]
my_tuple = (4,4,6,5,8,9,9,2,0,1)
my_set = {9,2,6,5}
my_dict = {'f':8,'z':9,'y':1, 'k':5}

def remove_duplicates(list:list) -> list:
  return list(set(list))

def list_counts(list:list) -> dict:
  return {key: list.count(key) for key in set(list)}

def reverse_dict(d:dict) -> dict:  
  reverseDict = {}
  for keys in d:
    values = d[keys]
    reverseDict[values] = keys
  return reverseDict
