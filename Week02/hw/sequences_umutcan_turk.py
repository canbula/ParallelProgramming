my_list = ["keyboard","mouse","laptop","mousepad","headset","mouse"]
my_tuple = ("2", "Hyundai",5.4,"Umut")
my_set = {"C#","C#","JAVA","JAVASCRIPT","PHP"}
my_dict = {
    "keyboard": 150,
    "mouse": 100,
    "laptop": 20000,
    "mousepad":20,
    "headset":120
}

def remove_duplicates(list_instance):
    new_list = []
    for key in list_instance:
        if key not in new_list:
            new_list.append(key)
    return new_list

def list_counts(list):
    counts_dict = {}
    for item in list:
        if counts_dict.get(item):
            counts_dict[item] += 1
        else:
            counts_dict[item] = 1
    return counts_dict

def reverse_dict(my_dict):
    reversed_dict = {}
    for key, value in my_dict.items():
        reversed_dict[value] = key
    return reversed_dict

