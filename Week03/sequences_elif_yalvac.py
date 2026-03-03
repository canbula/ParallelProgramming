def remove_duplicates(seq: list) -> list:
    return list(set(seq))


def list_counts(seq: list) -> dict:
    from collections import Counter
    return dict(Counter(seq))


def reverse_dict(d: dict) -> dict:
    from collections import defaultdict
    rev = defaultdict(list)
    for k, v in d.items():
        rev[v].append(k)
    return dict(rev)
