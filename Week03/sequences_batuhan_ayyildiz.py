# kopyaları silen fonksiyon
def remove_duplicates(seq: list) -> list:
    return list(dict.fromkeys(seq))


# list sayısını fonksiyonu
def list_counts(seq: list) -> dict:
    counts = {}
    for item in seq:
        counts[item] = counts.get(item, 0) + 1
    return counts



# dictionaryleri ters çeviriyor fonksiyonu
def reverse_dict(d: dict) -> dict:
    reversed_dict = {}
    for key, value in d.items():
        reversed_dict[value] = key  # Sonuncusu aynı değere sahip olan öğe overwrite eder
    return reversed_dict
