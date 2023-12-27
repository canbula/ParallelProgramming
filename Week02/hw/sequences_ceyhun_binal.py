my_list = ["Max Verstappen","Sergio Perez", "Lando Norris", "Carlos Jr. Sainz","Sergio Perez","Charles Leclerc","Max Verstappen", "Carlos Jr. Sainz","Lewis Hamilton", "Lando Norris"]
my_tuple = ("Redbull Racing", "Ferrari", "McLaren","Mercedes", "Ferrari", "McLaren")
my_set = {"Christian Horner", "Toto Wolff", "Guenther Steiner", "Frederic Vasseur"}
my_dict = {1: "Max Verstappen", 11: "Sergio Perez", 4: "Lando Norris", 1: "Max Verstappen", 55: "Carlos Jr. Sainz", 4: "Lando Norris",16: "Charles Leclerc"}


def remove_duplicates(seq: list) -> list:
    return list(set(seq))
    
result = remove_duplicates(my_list)
print(result)

def list_counts(seq: list) -> dict:
    return {item: seq.count(item) for item in set(seq)}

result = list_counts(my_list)
print(result)

def reverse_dict(d: dict) -> dict:
    return {value: key for key, value in d.items()}

reversed_dict = reverse_dict(my_dict)
print(reversed_dict)
