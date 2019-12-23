# mad libs.py
# Author: Tan Yi Xiang
# Source: Automate the Boring stuff with python Ch. 8 Project

import re

"""Reads in text files and lets the user add their own text anywhere 
the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file."""

ADJECTIVE = 'ADJECTIVE'
VERB = 'VERB'
NOUN = 'NOUN'
ADVERB = 'ADVERB'


def getWord(wordType):
    """Request user for new word input
         Args:
             wordType (str): The type of word to be changed eg: Adjective,Verb etc
         Returns:
             The word to replace the keyword with.
         """
    if (wordType == ADJECTIVE) or (wordType == ADJECTIVE):
        newWord = input('Enter an ' + wordType.lower() + ":\n")
        return newWord
    else:
        newWord = input('Enter a ' + wordType.lower() + ":\n")
        return newWord


def changeKeywords(madLibsString):
    """Detects the words ADJECTIVE, NOUN, ADVERB, or VERB in the text file and request the user to change them.
      Args:
          madLibsString (str): The text to be altered in the text file
      Returns:
          The new text after the change
      """
    for word in madLibsString.split():
        word = re.sub('[^A-Za-z0-9]+', '', word)
        if word == ADJECTIVE:
            madLibsString = madLibsString.replace(word, getWord(ADJECTIVE), 1)
        elif word == VERB:
            madLibsString = madLibsString.replace(word, getWord(VERB), 1)
        elif word == NOUN:
            madLibsString = madLibsString.replace(word, getWord(NOUN), 1)
        elif word == ADVERB:
            madLibsString = madLibsString.replace(word, getWord(ADVERB), 1)
        else:
            continue
    return madLibsString


madLibsFile = open('Mad Libs.txt')
madLibsAnswer = open('Mad Libs Ans.txt', 'w')
madLibsContent = madLibsFile.read()
replacementString = changeKeywords(madLibsContent)
madLibsAnswer.write(replacementString)

madLibsFile.close()
madLibsAnswer.close()
