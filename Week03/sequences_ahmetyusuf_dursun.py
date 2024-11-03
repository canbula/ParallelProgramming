def remove_duplicates (seq:list) -> list :
    return list(set(seq))

def list_counts(seq:list) -> dict :
    n = seq.count
    ndict={}
    for i in remove_duplicates(seq) :
        ndict[i]=n(i)
    return ndict

def reverse_dict(d:dict) -> dict:
    return {v: k for k, v in d.items()}
