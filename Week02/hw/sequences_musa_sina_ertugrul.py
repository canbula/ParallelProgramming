"""Musa Sina ERTUGRUL Homework

    This file contains sequences
    in Python. This homework has assigned
    by Bora Canbula

    my_list (list)
    my_tuple (tuple)
    my_set (set)
    my_dict (dict)
"""
from typing import (
    List, Dict, Set, Tuple
)


my_list : List = [2,3,4,5,7,8,9]
my_tuple : Tuple = (4,6,8,9,1,3)
my_set : Set = set([89,57,36,0,378,13])
my_dict : Dict = {  "abc":"190",
                    "dbc":"903"   }

def remove_duplicates(new_list: List)->List:
    """This function removes duplicates"""
    return list(set(new_list))

def list_counts(new_list: List)-> Dict:
    """This function counts items"""
    return {tmp_item : new_list.count(tmp_item) for tmp_item in new_list}

def reverse_dict(new_dict: Dict)-> Dict:
    """This function reverse dict"""
    return {
        tmp_value : tmp_key
        for tmp_key, tmp_value in zip(list(new_dict.keys()),list(new_dict.values()))
        }
