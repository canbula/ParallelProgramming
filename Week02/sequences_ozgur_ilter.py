my_list = ['a', 'b' ,'c','d','e','f','g']

my_tuple = (1,2,3,4,5,6,7,8)

my_set = {"Lesson","Instructor","Student","Book","Chapter"}

my_dic = {
    'Manisa' : 45,
    'Aydın' :9,
    'İzmir' : 35,
    'İstanbul':34

}

def remove_duplicates(list):
    unique_list = []

    for i in list:
        if i not in unique_list:
            unique_list.append(i)
        
    return unique_list


def list_counts(list):
   return{i: list.count(i) for i in list}

def reverse_dict(my_list):
    reversed_dict = {}
    for item in my_list.items():
        reversed_dict[item[1]] = item[0]
       
    return reversed_dict
