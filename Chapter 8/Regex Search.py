# Regex Search.py
# Author: Tan Yi Xiang
# Source: Automate the Boring stuff with python Ch. 8 Project

import os
import sys
import re

"""Search for a regex pattern in all txt files in a directory."""


def checkRegex(regex, textFileContents):
    """Check text file for regex matches
            Args:
                regex (Pattern[str]): The regex expression used to find matches.
                textFileContents(str) The contents of the text file.
            """
    regexMatch = regex.findall(textFileContents, re.I)
    print(regexMatch)


folderPath = input("Enter the directory path which you want to search for:\n")
if not os.path.isdir(folderPath):
    print("The directory does not exist")
    sys.exit()

regexExpressionString = input('Enter the regex expression to search for:\n')
regexExpression = re.compile(regexExpressionString)
for file in os.listdir(folderPath):
    if file.endswith('.txt'):
        textFilePath = os.path.join(folderPath, file)
        textFile = open(textFilePath, 'r+')
        textFileString = textFile.read()
        checkRegex(regexExpression, textFileString)
