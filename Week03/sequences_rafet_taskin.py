def remove_duplicates(l):
    return list(dict.fromkeys(l))

def list_counts(l):
    counts = {}
    for item in l:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts

def reverse_dict(d):
    reversed_d = {}
    for key, value in d.items():
        reversed_d[value] = key
    return reversed_d
