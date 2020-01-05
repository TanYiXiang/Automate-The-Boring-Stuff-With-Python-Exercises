# Blank Row Inserter.py
# Author: Tan Yi Xiang
# Source: Automate the Boring stuff with python Ch. 12 Project

import openpyxl

excelFilePath = input('Input the path of the excel file(with .xlsx extension):\n')
rowNo = input('Which row would you like to add blank rows from:\n')
blankRowNo = input('How many blank row would you like to add:\n')

workbook = openpyxl.load_workbook(excelFilePath)
sheet = workbook.active

sheet.insert_rows(int(rowNo), int(blankRowNo))
workbook.save(excelFilePath)
print('Blank rows inserted')
