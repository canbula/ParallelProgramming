my_list=[1,5,7,2,3,5,7,2,4,2,0,6,5,8,3,2,2]
my_tuple=(6,2,4,7,2,7,8,3,2)
my_set={1,3,6,8,2,5}
my_dict={'b':5,'a':8,111:'gdsf',10:'k'}

def remove_duplicates(input_:list) -> list:
  return list(set(input_))

def list_counts(input_:list) -> dict:
  ret={}
  for i in input_:
    if i not in ret:
      ret[i]=1
    else:
      ret[i]+=1
  return ret

def reverse_dict(input_:dict) -> dict:
  ret={}
  for i in input_:
    ret[input_[i]]=i
  return ret

"""
###################################
        Furkan Soylek
https://leetcode.com/TB09/
https://github.com/TIMEBANDIT11111
###################################
"""
