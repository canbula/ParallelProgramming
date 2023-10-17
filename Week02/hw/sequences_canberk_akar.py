my_list  = ["a","b","c","d","e"]
my_tuple = ("canberk","akar",25)
my_set   = {"honda","toyota","fiat","fiat"}
my_dict={
    "name"     :"The Sopranos",
    "director" :"Tim Van Patten",
    "year"     :1998
}

def remove_duplicates(list):
    dub=[]
    for item in list:
        if item not in dub:
            dub.append(item)
    return dub

def list_counts(list):
   dictionary = {}
   for item in list:
      if item in dictionary:
        dictionary[item] += 1
      else:
        dictionary[item] = 1
   return dictionary

def reverse_dict(dictionary):
    dict = {}
    for item in dictionary.items():
        dict[item[1]] = item[0]
    return dict
