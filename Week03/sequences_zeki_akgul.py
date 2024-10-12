def remove_duplicates(seq: list):
    for index, number in enumerate(seq):
        while seq.count(number) > 1:
            seq.remove(number)
          
    return seq

def list_counts(seq: list):
    dict = {}
    for index, number in enumerate(seq):
        dict.update({number: seq.count(number)})

    return dict

def reverse_dict(d: dict):
    new_dict = {}
    for key, value in d.items():
        new_dict.update({value:key})

    return new_dict
