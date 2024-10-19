
def remove_duplicates(seq: list) -> list:
    return list(set(seq))


def list_counts(seq: list) -> dict:
    result = dict.fromkeys(seq, 0)
    for i in seq:
        result[i] += 1
    return result


def reverse_dict(d: dict) -> dict:
    result = {}
    for i in d.items():
        result[i[1]] = i[0]
    return result

