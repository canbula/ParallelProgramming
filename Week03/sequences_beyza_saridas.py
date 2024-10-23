# Function to remove duplicates from a list
def remove_duplicates(seq: list) -> list:
    return list(set(seq))

# Function to count occurrences of each item in a list
def list_counts(seq: list) -> dict:
    counts = {}
    for item in seq:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts

# Function to reverse keys and values of a dictionary
def reverse_dict(d: dict) -> dict:
    return {v: k for k, v in d.items()}
