my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_set = {1, 2, 3, 4, 5}
my_dict = {1: "California Love", 2: "West Coast",
           3: "Long Beach", 4: "Dr. Dre", 5: "Hollywood Dream"}


def remove_duplicates(my_list: list) -> list:
    return list(set(my_list))


def list_counts(my_list: list) -> dict:
    return {item: my_list.count(item) for item in set(my_list)}


def reverse_dict(my_dict: dict) -> dict:
    return {value: key for key, value in my_dict.items()}
