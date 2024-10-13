def remove_duplicates(seq: list) -> list:

    return list(set(seq))

def list_counts(seq: list) -> dict:
    
    return {i: seq.count(i) for i in set(seq)}

def reverse_dict(d: dict) -> dict:

    return {v: k for k, v in d.items()}
