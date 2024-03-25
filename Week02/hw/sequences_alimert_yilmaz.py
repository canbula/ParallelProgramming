my_list = ["audi","Mercedes","audi","bmw"]

my_tuple = (2,3,'alimert')

my_set = {"Aws", "Docker" ,"Kubernates","Docker"}

my_dict = {
            "name": "Amazon",
            "employers": 300,
             
          }


def remove_duplicates(list):
    no_duplicates = []

    for item in list:
        if item not in no_duplicates:
            no_duplicates.append(item)

    return no_duplicates


def list_counts(list):
   dict = {}

   for item in list:
      if item in dict:
        dict[item] += 1
      else:
        dict[item] = 1

   return dict


def reverse_dict(dictionary):
    reversed_dict = {}
    for key, value in dictionary.items():
        if value not in reversed_dict:
            reversed_dict[value] = key
    return reversed_dict

print(remove_duplicates(my_list))
print(list_counts(my_list))
print(reverse_dict(my_dict))