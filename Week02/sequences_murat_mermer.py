my_list = ["istanbul","ankara","izmir","sivas","bolu","ankara"]
my_tuple = ("15", "jbl",1.3,"mermer")
my_set = {"eregli","şişecam","tüpraş","aselsan","YTD."}
my_dict = {
    "eregli": 350,
    "şişecam": 180,
    "tüpraş": 450,
    "aselsan":2500,
    "YTD":0
}

def remove_duplicates(list_):
    new_list = []
    for key in list_:
        if key not in new_list:
            new_list.append(key)
    return new_list

def list_counts(list_):
    counts = {}
    for item in list_:
        if counts.get(item):
            counts[item] += 1
        else:
            counts[item] = 1
    return counts


def reverse_dict(my_dict):
    reversed_dictionary = {}
    for key, value in my_dict.items():
        reversed_dictionary[value] = key
    return(reversed_dictionary)

