def remove_duplicates(seq: list) -> list:
    seq_set = set(seq)
    return list(seq_set)

def list_counts(seq: list) -> dict:
    seq_set = set(seq)
    seq_dict = {key : 0 for key in seq_set}

    for i in range(len(seq)):
        seq_dict[seq[i]] += 1

    return seq_dict

def reverse_dict(d: dict) -> dict:
    d_reverse = dict()
    for i in d:
        value = d[i]
        d_reverse.update({value : i})
    return d_reverse
