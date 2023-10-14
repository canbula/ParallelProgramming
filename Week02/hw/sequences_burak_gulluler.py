my_list = [1, 2, 3, 3, 3, 4, 5, 5, 6, 7]

my_tuple = (1, 2, 3, "Hello", "World")

my_set = {"SpongeBob SquarePants", "Patrick Star", "Squidward Tentacles"}

my_dict = {
    "dizi": "komedi",
    "spor": "basketbol",
    "yazar": "dostoyevski",
    "yemek": "pizza",
}

def remove_duplicates(my_list):
    return list(set(my_list))

def list_counts(my_list):
    return {i: my_list.count(i) for i in my_list}

def reverse_dict(my_dict):
    return {v: k for k, v in my_dict.items()}
