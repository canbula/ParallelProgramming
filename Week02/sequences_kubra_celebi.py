my_list=[9,10,True,"k"]
my_tuple=(3,5,7)
my_set={2,4,1}
my_dict={"name" :"Kubra",
        "surname" : "Celebi",
        "city":"Kocaeli"}

def remove_duplicates(first_list):
empty_list=[]
for item in first_list:
  if item not in empty_list:
    empty_list.appent(item)

return empty_list

def list_counts(first_list):
  dict_counts={}
  for item in first_list:
      if item in dict_counts:
          dict_counts[item] +=1
      else:
          dict_counts[item]=1
    return dict_counts

def reverse_dict(first_dict):
  containing_inversions={}
  for key, value in first_dict.items():
    containing_inversions[value] = key
  return containing_inversions
        
      
