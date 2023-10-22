my_list = [1, "League of Legends is an addicting game", True, 1.2, 1j, [1, 2]]

my_tuple = (1, "I have never played League of Legends in my life", False, 1.2, 1j, (1, 2))

my_set = {1, "I am not going to ruin my life with a LoL addiction", False, frozenset({1})}

my_dict = {
    "name": "Sinem",
    "age": 22,
    "hobbies": "Not League of Legends"
}

# Function to remove duplicates from a list
def remove_duplicates(input_list):
    new_list = []
    for item in input_list:
        if item not in new_list:
            new_list.append(item)
    input_list.clear()
    input_list.extend(new_list)

# Example use
remove_duplicates(my_list)
print(my_list)

# Function to count the occurrence of each item in a list
# and return it as a dictionary
def list_counts(input_list):
    new_dict = {}
    for item in input_list:
        if item in new_dict:
            new_dict[item] += 1
        else:
            new_dict[item] = 1
    return new_dict

# Example use
print(list_counts(my_list))

# Function to reverse a dictionary and switch the keys and values
def reverse_dict(input_dict):
    new_dict = {}
    for key, value in input_dict.items():
        new_dict[value] = key
    return new_dict

# Example use
print(reverse_dict(my_dict))
