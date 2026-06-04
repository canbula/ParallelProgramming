def remove_duplicates(seq: list) -> list:
    return list(dict.fromkeys(seq))


def list_counts(seq: list) -> dict:
    counts = {}

    for item in seq:
        counts[item] = counts.get(item, 0) + 1

    return counts


def reverse_dict(dct: dict) -> dict:
    return {value: key for key, value in dct.items()}
