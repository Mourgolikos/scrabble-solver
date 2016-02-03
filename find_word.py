__author__ = 'Triantafyllos Paschaleris'

from letters import lettersInHand, lettersPlayed
from prepare_words_list import filename

lettersInHand = ["Α", "Β", "Γ", "Ο", "*"] #debugging

maxWordLength = len(lettersInHand) # TODO: adjust it for longer legth because of extra letters from on-board

wordList = []
with open(filename ,mode='r', encoding="utf-8") as f:
    wordList = f.read().splitlines()

sorted(wordList, key=len) # Although the file is already sorted, in order to be sure (due to possible latter file-editing) we re-sort the list

for word in wordList:
    if len(word) > maxWordLength: break # Since the list is sorted by the words length, then we don't have to look further.
    for letter in lettersInHand:
        if letter == "*": continue # "*" is the empty (wildcard) square
        if letter not in word: break
    else: # None of the break condition are met, so the word does match!
        print(word)#debugging
