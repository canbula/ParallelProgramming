def remove_duplicates(seq: list) -> list:
    """Bu fonksiyon bir listedeki tekrar eden elemanları siler."""
    return list(dict.fromkeys(seq))

def list_counts(seq: list) -> dict:
    """Bu fonksiyon listedeki her bir elemanın kaç kez geçtiğini sayar."""
    counts = {}
    for item in seq:
        counts[item] = counts.get(item, 0) + 1
    return counts

def reverse_dict(d: dict) -> dict:
    """Bu fonksiyon bir sözlüğün anahtar ve değerlerini yer değiştirir."""
    return {value: key for key, value in d.items()}
