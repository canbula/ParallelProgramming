my_list = [11, 1, 1101, 110011]
my_tuple = (1, 11, 11, 1)
my_set = {"F", "C"}
my_dict = {
    "sanma şahım": "herkesi sen",
    "herkesi sen": "dost mu sandın",
    "sadıkhane": "belki ol",
    "yar olur": "ağyar olur",
}


def remove_duplicates(seq: list) -> list:
    return list(set(seq))


def list_counts(seq: list) -> dict:
    return {item: seq.count(item) for item in set(seq)}


def reverse_dict(d: dict) -> dict:
    return {value: key for key, value in d.items()}


initial_key_order = ' '.join([k for k in my_dict.keys()])
modified_key_order = ' '.join([k for k in reverse_dict(my_dict).keys()])

"""
print(initial_key_order)
print(modified_key_order)

Output:
sanma şahım herkesi sen sadıkhane yar olur
herkesi sen dost mu sandın belki ol ağyar olur
"""
