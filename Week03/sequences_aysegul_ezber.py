
def remove_duplicates(seq: list) -> list:
   
    return list(set(seq))


def list_counts(seq: list) -> dict:
    
    counts = {}
    for item in seq:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts

def reverse_dict(d: dict) -> dict:
 
    return {v: k for k, v in d.items()}

my_list = [1, 2, 2, 3, 4, 4, 4, 5]
print("Tekrarlanmayan liste:", remove_duplicates(my_list))
print("Eleman sayıları:", list_counts(my_list))

my_dict = {'a': 1, 'b': 2, 'c': 3}
print("Ters çevrilmiş sözlük:", reverse_dict(my_dict))
