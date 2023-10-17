my_list = ["apple", "melon", "peach", 20, 'd', "apple", 2]
my_tuple = (1, 2, 3)
my_set = {4, 4, 2}
my_dict = {1: "ziraat", 2: "is", 3: "garanti"}

"""This function removes duplicates."""
def remove_duplicates(mylist: list) -> list:
    return list(set(mylist))

"""This function counts items."""
def list_counts(moaList: list) -> dict:
    counts = {}
    for moa in moaList:
        if moa in counts:
            counts[moa] += 1
        else:
            counts[moa] = 1
    return counts

"""This function reverse dict."""
def reverse_dict(input_moa: dict) -> dict:
    reversed_dict = {element: key for key, element in input_moa.items()}
    return reversed_dict

