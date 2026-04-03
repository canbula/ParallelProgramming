from collections import Counter

def remove_duplicates(seq: list) -> list:
   
    return list(dict.fromkeys(seq))

def list_counts(seq: list) -> dict:
    
    return dict(Counter(seq))

def reverse_dict(d: dict) -> dict:
   
    return {value: key for key, value in d.items()}
