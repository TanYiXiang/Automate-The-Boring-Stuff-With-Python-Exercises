"""Prints a nicely aligned table from a list of strings."""


def printTable(inputList):
    """Initialize a column width list to store the longest string length from each inner list."""
    colWidth = [0] * len(inputList)

    """Find longest word length in each inner list and store it in the column width list."""
    for i in range(len(inputList)):
        colWidth[i] = len(max(inputList[i], key=len))

    """Print the list in table format padded according to the column width value."""
    for x in range(len(inputList[0])):
        for y in range(len(inputList)):
            print(inputList[y][x].rjust(colWidth[y]), end=' ')
        print()


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
