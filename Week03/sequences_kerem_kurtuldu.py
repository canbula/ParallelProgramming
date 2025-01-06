def remove_duplicates(seq: list) -> list:
    # Remove duplicates by iterating and adding unique items to a new list
    unique_items = []
    for item in seq:
        if item not in unique_items:
            unique_items.append(item)
    return unique_items

def list_counts(seq: list) -> dict:
    # Count occurrences using a dictionary and a loop
    counts = {}
    for item in seq:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts

def reverse_dict(d: dict) -> dict:
    # Reverse dictionary using a loop
    reversed_dict = {}
    for key, value in d.items():
        reversed_dict[value] = key
    return reversed_dict
