def remove_duplicates(seq:list) -> list:
   return list(set(seq))


def list_counts(seq: list) -> dict:
    counts = {}
    for item in seq:
        counts[item] = counts.get(item, 0) + 1
    return counts


def reverse_dict(d: dict) -> dict:
    return {v: k for k, v in d.items()}
