def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.
    
    returns: int, how many values are in the dictionary.
    '''
    #You Code Here
    num = 0
    for i in aDict:
        num += len(aDict[i])
        #for j in aDict[i]:
        #    num += 1
    return num