def unique_items(seq):
    return list(set(seq))

def item_frequencies(seq):
    d = {}
    for i in seq:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d

def reverse_dict(d):
    nd = {}
    for i, h in d.items():
        nd[h] = i
    return nd
