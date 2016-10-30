def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    i = 1
    result = base
    if exp <= 0:
        result = 1
    while i < exp:
        result *= base
        i += 1
        
    return result