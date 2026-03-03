def remove_duplicates( seq:list ) -> list:
  new_list = []
  for i in seq:
    if i not in new_list:
      new_list.append(i)

  return new_list
  

def list_counts(seq: list) -> dict:
    counts = {}
    for item in seq:
        counts[item] = counts.get(item, 0) + 1
  
  return counts



def reverse_dict(d: dict) -> dict:
    new_d = {}
    for k, v in d.items():
        new_d[v] = k 
  return new_d
