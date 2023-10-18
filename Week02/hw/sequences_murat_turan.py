my_list = [1,2,3,3,4,5,6]
my_tuple = (7,8,9)
my_set = {"","",""}
my_dict = {"name": "Murat" ,"surname": "Turan","age": 21}


def remove_duplicates(my_list):
    new_list=[]
    for item in my_list:
      if item not in new_list:
          new_list.append(item)

    return new_list

def list_counts(my_list):
    counter = {}
    for i in my_list:
      if i in counter:
        counter[i] +=1
      else:
        counter[i]=1
    return counter


def reverse_dict(dictionary):
    return {value: key for key, value in dictionary.items()}
