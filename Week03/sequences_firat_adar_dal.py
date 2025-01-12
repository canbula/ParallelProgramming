def remove_duplicates(seq: list) -> list:
    # Listeden tekrarları kaldırır ve sıralamayı korur.
    unique_items = []
    for item in seq:
        if item not in unique_items:
            unique_items.append(item)
    return unique_items

def list_counts(seq: list) -> dict:
    # Listedeki her elemanın kaç kez geçtiğini sayar.
    counts = {}
    for item in seq:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts

def reverse_dict(d: dict) -> dict:
    # Sözlükteki anahtarları ve değerleri ters çevirir.
    reversed_dict = {}
    for key, value in d.items():
        reversed_dict[value] = key
    return reversed_dict
