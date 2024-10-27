def remove_duplicates(seq:list)->list:
  """This function removes duplicates from a list"""
  new_list = []
  for i in seq:
    if not i in new_list:
      new_list.append(i) 
  
  
  
  return new_list
     
 

def list_counts(seq:list)->dict:
  my_dict={}
  
  for i in seq:
    my_dict[i] = seq.count(i)
    
  return my_dict

def reverse_dict(d:dict) -> dict:
  new_dict={}
  for x,y in dict.items():
    new_dict.update({y:x})
  
  return new_dict
