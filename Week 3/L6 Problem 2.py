def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    other = ()
    for i in range(len(aTup)):
        if i % 2 == 0:
            other = other + (aTup[i],)
    return other