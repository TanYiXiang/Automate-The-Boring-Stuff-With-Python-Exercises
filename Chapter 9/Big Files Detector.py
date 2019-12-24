# Big File Detector.py
# Author: Tan Yi Xiang
# Source: Automate the Boring stuff with python Ch. 9 Project

"""Walk a folder tree and print the names of files above a chosen size."""

import os

folderPath = input("Enter the folder path to check:\n")
try:
    minFileSize = int(input("Enter the minimum file size to search for (in MB):\n"))
    assert minFileSize >= 0
except ValueError:
    print("File size must be an integer")
except AssertionError:
    print("File size must be a positive number")

if os.path.exists(folderPath):
    for folderName, subFolders, fileNames in os.walk(folderPath):
        for file in fileNames:
            fileSize = os.path.getsize(os.path.join(folderName, file))
            if fileSize >= (minFileSize * 1000000):
                print(os.path.join(folderPath, file))

else:
    print("Sorry the folder path is invalid.")
