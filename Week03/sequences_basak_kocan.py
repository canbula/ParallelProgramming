def remove_duplicates(seq: list) -> list:
    a_list = list(set(seq))
    for i in range(len(a_list)):
        for j in range(i + 1, len(a_list)):
            if a_list[i] == a_list[j]:
                a_list.pop(j)
    return a_list

def list_counts(seq: list) -> dict:
    b_list = list(set(seq))
    b_dict = {}
    for i in range(len(b_list)):
        count = 0
        for j in range(len(seq)):
            if b_list[i] == seq[j]:
                count += 1
        b_dict[b_list[i]] = count
    return b_dict

def reverse_dict(d: dict) -> dict:
    c_dict = {}
    for key, value in d.items():
        c_dict[value] = key
    return c_dict
