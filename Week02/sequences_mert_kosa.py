my_list = [1,1,2,2,3,4]
my_tuple = (1,2,3,4,5,6)
my_set = {1,2,3,4,5,6,7,8}
my_dict = {"one":1, "two":2, "three":3, "four":4 }

def remove_duplicates( anyList : list ) -> list :
    return list(set(anyList))

def list_counts(my_list: list) -> dict:
    return {index: seq.count(index) for index in set(my_list)}

def reverse_dict(my_dict: dict) -> dict:
    return {value: key for key, value in my_dict.items()}

