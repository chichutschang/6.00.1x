def isVowel(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    # Your code here
    if (str.lower(char) == 'a' or str.lower(char) == 'e' or str.lower(char) == 'i' or str.lower(char) == 'o' or str.lower(char) == 'u'):
        return True
    else:
        return False
