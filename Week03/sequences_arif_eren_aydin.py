def remove_dublicates(seq: list) -> list :
    yeni_liste=[]
    for i in seq:  
        if not yeni_liste.count(i):
            yeni_liste.append(i)
    return yeni_liste
def list_counts(seq: list) -> dict:
    dictionary = {}
    for i in seq:
        dictionary.update({i: seq.count(i)})
    return dictionary
def reverse_dict (d: dict) -> dict:
    reversed_dict = {}
    for key, value in d.items():
        reversed_dict[value] = key  
    return reversed_dict
