def remove_duplicates(seq: list) -> list:
    uniq_list = []
    for i in seq:
        if i not in uniq_list:
            uniq_list.append(i)
    return uniq_list
        
def list_counts(seq : list) -> dict:
    counts = {}
    for i in seq:
        counts[i] = counts.get(i, 0) + 1
    return counts

def reverse_dict(d: dict) -> dict:     
    res = {}
    for k ,v in d.items():
        res[v] = k
    return res         
