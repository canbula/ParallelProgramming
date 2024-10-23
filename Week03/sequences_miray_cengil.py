from collections import defaultdict

def remove_duplicates(seq: list) -> list:
    unique_list = []
    for number in seq:
        if number not in unique_list:
            unique_list.append(number)
    return unique_list

def list_counts(seq: list) -> dict:
    counts = {}
    for item in seq:
        if item in counts:
            counts[item] += 1
        else: 
            counts[item] = 1
    return counts

def reverse_dict(d: dict) -> dict:
    new_dict = {}
    for key, value in d.items():
        new_dict[value] = key 
    return new_dict
