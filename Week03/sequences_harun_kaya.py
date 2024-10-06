def remove_duplicates(seq: list) -> list:
    return list(dict.fromkeys(seq))


def list_counts(seq: list) -> dict:
    return {item: seq.count(item) for item in seq}


def reverse_dict(seq: dict) -> dict:
    return {value: key for key, value in seq.items()}
