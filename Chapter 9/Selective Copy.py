# Selective Copy.py
# Author: Tan Yi Xiang
# Source: Automate the Boring stuff with python Ch. 9 Project

"""Walk through a folder tree and copy all files of a particular extension."""
import shutil
import os

sourcePath = input("Enter the source directory path where you would like to copy from :\n")
fileExtension = input("Enter the file extension types you wish to copy eg pdf:\n")
destinationPath = input("Enter the destination directory path to copy files to:\n")
hasFileType = False

for folderName, subFolders, fileNames in os.walk(sourcePath):
    for fileName in fileNames:
        if fileName.lower().endswith(fileExtension):
            shutil.copy(os.path.join(folderName, fileName), destinationPath)
            hasFileType = True
            print(fileName + ' copied to. ' + destinationPath)

if hasFileType:
    print("Success, all " + fileExtension + " files have been copied to " + destinationPath)
else:
    print("Sorry, no file of type " + fileExtension + " have been found in " + sourcePath)
