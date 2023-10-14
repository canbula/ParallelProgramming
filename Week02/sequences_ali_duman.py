my_list = [2, 4, 8, 16, 32, 64, 128, 256]

my_tuple = (11, 33, 55, "The", "Blacklist")

my_set = {"Raymond Reddington", "Elizabeth Keen", "Glen Carter"}

my_dict = {
    "one": "I",
    "two": "Had",
    "three": "Bullets",
    "four": "He",
    "five": "Had",
    "six": "Words",
}


def remove_duplicates(my_list):
    return list(set(my_list))


def list_counts(my_list):
    return {item: my_list.count(item) for item in my_list}


def reverse_dict(my_dict):
    return {value: key for key, value in my_dict.items()}
