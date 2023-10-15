def find_unique_elements(input_list: list) -> list:
    return list(set(input_list))

def count_element_occurrences(input_list: list) -> dict:
    element_counts = {}
    
    for element in input_list:
        if element in element_counts:
            element_counts[element] += 1
        else:
            element_counts[element] = 1
    
    return element_counts

def reverse_dict(input_dict: dict) -> dict:
    reversed_dict = {}

    for key, value in input_dict.items():
        reversed_dict[value] = key
    
    return reversed_dict

my_list = [10, "Different List", 52.600, True, 23 + 5j]
my_tuple = ("M", "Fabulous", "List")
my_set = {True, 1}
my_dict = {
    "full_name": "MEHMETANIL",
    "nickname": "KraLex",
    "age": 24
}

unique_list = find_unique_elements(my_list)
occurrences = count_element_occurrences(my_list)
reversed_dict = reverse_dict(my_dict)

print("Unique Elements:", unique_list)
print("Element Occurrences:", occurrences)
print("Reversed Dictionary:", reversed_dict)
