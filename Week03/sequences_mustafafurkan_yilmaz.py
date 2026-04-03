def remove_duplicates(lst: list) -> list:
    """
    Listeden tekrar eden elemanları kaldırır, sırayı korur.
    """
    seen = []
    for item in lst:
        if item not in seen:
            seen.append(item)
    return seen


def list_counts(lst: list) -> dict:
    """
    Listedeki her elemanın kaç kez geçtiğini sayar.
    """
    counts = {}
    for item in lst:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts


def reverse_dict(d: dict) -> dict:
    """
    Sözlüğün anahtar ve değerlerini ters çevirir.
    Aynı değere sahip birden fazla anahtar varsa, son anahtarı tutar.
    """
    reversed_d = {}
    for key, value in d.items():
        reversed_d[value] = key
    return reversed_d
