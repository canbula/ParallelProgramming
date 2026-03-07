def remove_duplicates(seq: list) -> list:
    return list(set(seq))
  
def list_counts(seq: list) -> dict:
    counts = dict.fromkeys(seq, 0)
    for item in seq:
        counts[item] += 1      
    return counts
  
def  reverse_dict(seq: dict) -> dict:
    reversed_dict = {}  
    for key, value in seq.items():
        reversed_dict[value] = key
    return reversed_dict







  
