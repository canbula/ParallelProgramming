def remove_duplicates(seq: list) -> list:
    result = []

    for item in seq:
        if item not in result:
            result.append(item)

    return result


def list_counts(seq: list) -> dict:
    result = {}

    for item in seq:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1

    return result


def reverse_dict(d: dict) -> dict:
    result = {}

    for key, value in d.items():
        result[value] = key

    return result
