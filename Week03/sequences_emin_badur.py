def remove_duplicates(seq: list) -> list :
  #This function remove duplicates from list. But we could use the set method to same purpose too.
    current_index = 0
    while current_index < len(seq) - 1 :
        if seq[current_index] == seq[current_index + 1]: 
            del seq[current_index + 1]
        else :
            current_index += 1 
    return seq

def list_counts(seq: list) -> dict:
  return {item: seq.count(item) for item in seq}

def reverse_dict(d: dict) -> dict:
    new_dict = {}
    for key, value in d.items():
        new_dict[value] = key
    return new_dict




              
           
