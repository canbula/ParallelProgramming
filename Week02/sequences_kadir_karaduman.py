my_list = ["Ali", "Ahmet", "Ayşe", "Fatma", "Ali"]
my_tuple = (1, 2, 3, 4, 5, 6)
my_set = {"Muradiye", "Yunusemre", "Şehzadeler", "Soma", "Ahmetli"}
my_dict = {"name": "Kadir",
           "surname": "Karaduman",
           "age": 21,
           "department": "Computer Engineering",
          }

def list_duplicates(input_list):
    return list(set(input_list))

def count_items(exp_list):
    item_count = {}
    for item in exp_list:
        if item in item_count:
            item_count[item] += 1
        else:
            item_count[item] = 1
    return item_count

def reverse_dict(dict):
    return {value: key for key, value in dict.items()}
