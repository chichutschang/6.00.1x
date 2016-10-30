# 6.00x Problem Set 4A Template
#
# The 6.00 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
# Modified by: Sarina Canelake <sarina>
#

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

#
# Problem #1: Scoring a word
#
def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    # TO DO ... <-- Remove this comment when you code this function
    score = 0
    
    if int(n) == int(len(word)):
        bonus = 50
    else:
        bonus = 0        
    
    for c in word:              
            score += SCRABBLE_LETTER_VALUES[c]
            
    return int(score) * int(len(word)) + int(bonus)

#
# Problem #2: Update a hand by removing letters
#
def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # TO DO ... <-- Remove this comment when you code this function
    letters = ""
    test = hand.copy()
    
    for x in word:
        if x in test:
            test[x] = test.get(x, 0) - 1
              
    return test
       
#
# Problem #3: Test word validity
#
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    test = hand.copy()

    for x in word:
        if test.get(x): 
            test[x] = test[x] - 1
        else:
            return False

    if word not in wordList:
        return False
        
    else:
        return True

def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    returns: string or None
    """
    # BEGIN PSEUDOCODE (available within ps4b.py)    
    # Create a new variable to store the maximum score seen so far (initially 0)
    maxScore = 0
    
    # Create a new variable to store the best word seen so far (initially None)  
    bestWord = None
    
    # For each word in the wordList
    for word in wordList:
    
        # If you can construct the word from your hand
            if isValidWord(word, hand, wordList) == True:
            # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
                
                score = getWordScore(word, n)
                # Find out how much making that word is worth
                
                # If the score for that word is higher than your best score
                if score > maxScore:
             
                    # Update your best score, and best word accordingly
                    maxScore = score                    
                    bestWord = word
                
    # return the best word you found.
    return bestWord
