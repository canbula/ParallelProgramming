my_list = [1,2,3,4,5,6,7,1]
my_tuple = (1,2,3,4,5,"cengiz","hello")
my_set = {1,"hi",2,3,4}
my_dict = {"ad":"cengizhan", "soyad":"cam","yas":23}

def remove_duplicates(my_list):
    return list(set(my_list))

def list_counts(my_list):
    new_dict ={}
    for i in my_list:
        if i in new_dict:
            new_dict[i] +=1
        else:
            new_dict[i]=1    
    return(new_dict)

def reverse_dict(my_dict):
     new_dict = {}
     for k,v in my_dict.items():
       new_dict[v] = k
     return new_dict


  




  





