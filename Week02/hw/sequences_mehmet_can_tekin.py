my_list = [1,2,3,4]
my_tuple = (5,6,7)
my_set ={8,9,10}
my_dict= {"Honda": "Civic","Ford": "Focus"}


def remove_duplicates (seq:list):
    holder_list=[]
    my_mark=0
    for seq_exploler in range(seq.__len__()):
        for holder_explorer in range(holder_list.__len__()):
            if seq[seq_exploler]==holder_list[holder_explorer]:
                my_mark=1
        if my_mark==0:
            holder_list.append(seq[seq_exploler])
        else:
            my_mark=0
    seq=holder_list
    return seq


def list_counts (seq:list)->dict:
    dict_counts={}
    for seq_explorer in seq:
        if dict_counts.__contains__(seq_explorer):
            dict_counts[seq_explorer] +=1
        else:
            dict_counts[seq_explorer]=1
    return dict_counts


def reverse_dict(seq:dict):
    reversed_dict={value : key for key, value in seq.items()}
    return reversed_dict

