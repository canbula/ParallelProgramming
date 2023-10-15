my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_set = {1, 2, 3, 4, 5}
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

def remove_duplicates(input_list):
  return list(set(input_list))

def list_counts(input_list):
counts = {}
for item in input_list:
  if item in counts:
    counts[item] += 1
  else:
    counts[item] = 1
return counts

def reverse_dict(input_dict):  
    reversed_dict = {v: k for k, v in input_dict.items()}
    return reversed_dict

original_dict = {'apple': 1, 'banana': 2, 'cherry': 3}
reversed_dict = reverse_dict(original_dict)
print(reversed_dict)
