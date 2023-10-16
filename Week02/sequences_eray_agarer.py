my_list = ["apple", "pear", "banana", "strawberry","apple"]
my_tuple = ("linux", "windows",190316084, True)
my_set = {"html", "css" ,"javascript",2023,2023}  
my_dict = {
    "name": "eray",
    "surname":"agarer",
    "ID":190316084
}

def remove_duplicates(list):
    no_dublicate = []
    for item in list:
        if item not in no_dublicate:
            no_dublicate.append(item)
    return no_dublicate

def list_counts(list):
   counted_dict = {}

   for item in list:
      if item in counted_dict:
        counted_dict[item] += 1
      else:
        counted_dict[item] = 1

   return counted_dict

def reverse_dict(dict):
   reversed_dict = {value: key for key, value in dict.items()}
   return reversed_dict


