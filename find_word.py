__author__ = 'Triantafyllos Paschaleris'

from letters import lettersInHand, lettersPlayed, lettersValues
from prepare_words_list import filename

lettersInHand = ["Α", "Β", "Γ", "Ο", "*"] #debugging

maxWordLength = len(lettersInHand) # TODO: adjust it for longer legth because of extra letters from on-board


def calculateWordValue(_word=""):
    #the word is expected in format "ΑΒΓΟ.*" where the letters after the "." are those replaced by "*"  e.g. "ΑΒ*Ο.Γ"
    return sum(lettersValues[_letter] for _letter in word.split(".")[0])



wordList = []
with open(filename ,mode='r', encoding="utf-8") as f:
    wordList = f.read().splitlines()

sorted(wordList, key=len) # Although the file is already sorted, in order to be sure (due to possible latter file-editing) we re-sort the list

for word in wordList:
    if len(word) > maxWordLength: break # Since the list is sorted by the words length, then we don't have to look further.
    _lettersInHand = lettersInHand[:]# Create a new copy with the [:] instead of a reference, because of the latter .remove() method
    for letter in word:
        if letter == "*": continue # "*" is the empty (wildcard) square
        if letter not in _lettersInHand:
            if "*" in _lettersInHand:
                word = word.replace(letter,"*",1) + "."+letter
                _lettersInHand.remove("*") # "*" is the empty (wildcard) square, if we have one we use it now for this letter!
            else: break
        else:
            _lettersInHand.remove(letter)
    else: # None of the break condition are met, so the word does match!
        print(word, calculateWordValue(word))#debugging