my_list = ["Giorno Giovanna","Gold Experience",15]

my_tuple = (7,9,True)

my_set = {"NextJs", "NestJs" ,"GraphQL",9}

my_dict = {
            "name": "Semerkant",
            "author": "Amin Maalouf",
            "genre": "Historical Fiction"
          }


def remove_duplicates(list):
    unique_list = []

    for item in list:
        if item not in unique_list:
            unique_list.append(item)

    return unique_list


def list_counts(list):
   counted_dict = {}

   for item in list:
      if item in counted_dict:
        counted_dict[item] += 1
      else:
        counted_dict[item] = 1

   return counted_dict


def reverse_dict(dictionary):
    reversed_dict = {}
    for item in dictionary.items():
        reversed_dict[item[1]] = item[0]

    return reversed_dict
