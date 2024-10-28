def remove_duplicates(seq: list) -> list:

    return list(set(seq))


def list_counts(seq: list) -> dict:

    count = {}

    for i in seq:
        count[i] = seq.count(i)

    return count
 


def reverse_dict(d: dict) -> dict:

    reversed = {}

    for key, value in d.items():
        reversed[value] = key

    return reversed