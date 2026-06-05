def remove_dublicates(list_:list) ->list:
    mini_cache= set()
    will_returned=[]
    if(list_ ==[]):
        return []
    for i in range(len(list_)):
        if(list_[i] in mini_cache):
            pass
        else:
            mini_cache.add(list_[i])
            will_returned.append(list_[i])
    return will_returned

def list_counts(list_:list) ->dict:
    mini_cache= dict()
    if(list_ ==[]):
        return {}
    for i in range(len(list_)):
        if(list_[i] in mini_cache):
            mini_cache[list_[i]] += 1
        else:
            mini_cache[list_[i]] = 1
            
    return mini_cache

def reverse_dict(dict_:dict) ->dict:
    mini_cache= dict() 
    for key, value in dict_.items():
        mini_cache[value] = key
        
    return mini_cache
    

print(remove_dublicates([1, 2, 3, 3, 4, 5, 5, 5, 6]))
print(list_counts([1,1,1,1,1,1]))
print(reverse_dict({1: 1, 2: 1, 3: 1}))
