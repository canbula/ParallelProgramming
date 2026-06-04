def remove_duplicates(argList: list) :
    for i in argList:
        while argList.count(i) > 1:
            argList.remove(i)
    return argList
def list_counts(argList: list):
    retDict = {}
    for i in argList:
        if i in retDict:
            retDict[i] += 1
        else:
            retDict[i] = 1
    return retDict
def reverse_dict(argDict: dict):
    retDict = {}
    for i,j in argDict.items():
        retDict[j]=i
    return retDict

        
            
        
                    
                
