def isVowel2(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    # Your code here
    if str.lower(char) in ("a", "e", "i", "o", "u"):
        return True
    else:
        return False
