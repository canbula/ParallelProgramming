def unique_items(seq):
    return list(set(seq))

def item_frequencies(seq):
    d = {}
    for i in seq:
        try:
            d[i] += 1
        except:
            d[i] = 0
            d[i] += 1
                        
    return d

def reverse_dict(d):
    nd ={}
    for i,h in d.items():
        nd[h] = i
    return nd
