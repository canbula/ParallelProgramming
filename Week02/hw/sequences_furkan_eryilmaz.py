my_list = [42, "Heterogeneous List", 16.667, False, 27 + 8j]
my_tuple = ("A", "Homogeneous", "Tuple")
my_set = {True, 1}
my_dict = {
    "full_name": "REDACTED",
    "nickname": "Kolta",
    "age": 22
}

def remove_duplicates(list_argument: list) -> list:
    return [element for element in set(list_argument)]

def list_counts(list_argument: list) -> dict:
    element_counts = {}
    
    for element in list_argument:
        if element in element_counts:
            element_counts[element] += 1
        else:
            element_counts[element] = 1
    
    return element_counts

def reverse_dict(dict_argument: dict) -> dict:
    dictionary_reversed = {}

    for key, value in dict_argument.items():
        dictionary_reversed[value] = key
    
    return dictionary_reversed