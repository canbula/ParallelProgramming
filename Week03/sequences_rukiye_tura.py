def remove_duplicates(seq: list) -> list:
    seq = list(set(seq))
    return seq

def list_counts(seq:list) -> dict :
    t = seq.count    
    return {i: t(i) for i in remove_duplicates(seq)}

def reverse_dict(d: dict) -> dict:
    return {v: k for k, v in d.items()}
