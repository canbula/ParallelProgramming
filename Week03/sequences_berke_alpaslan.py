def remove_duplicates(seq: list) -> list:
    return list(set(seq))

def list_counts(seq: list) -> dict:
    seq_dict = {key : 0 for key in set(seq)}
    for i in range(len(seq)):
        seq_dict[seq[i]] += 1
    return seq_dict

def reverse_dict(d: dict) -> dict:
    d_reverse = dict()
    for key in d:
        value = d[key]
        d_reverse.update({value : key})
    return d_reverse
