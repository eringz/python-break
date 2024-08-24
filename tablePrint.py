'''
    Write a function named printTable() that takes a list of lists of strings 
    and displays it in a well-organized table with each column right-justified. 
    Assume that all the inner lists will contain the same number of strings. 
    For example, the value could look like this:
        tableData = [['apples', 'oranges', 'cherries', 'banana'],
        ['Alice', 'Bob', 'Carol', 'David'],
        ['dogs', 'cats', 'moose', 'goose']]
    Your printTable() function would print the following:
          apples Alice  dogs
         oranges   Bob  cats
        cherries Carol moose
          banana David goose
'''

tableData = [
                ['apples', 'oranges', 'cherries', 'banana'],
                ['Alice', 'Bob', 'Carol', 'David'],
                ['dogs', 'cats', 'moose', 'goose']
            ]

# Find longest characters in 
# colWidth = []
# temp = []
# for i in range(len(tableData)):
#     print('Table %s' % (i+1))
#     maxLength = 0
#     for j in range(len(tableData[i])):
#         characterLong = len(tableData[i][j])
#         if maxLength < characterLong:
#             maxLength = characterLong             
#     print('max length: %s' % maxLength)
#     colWidth.append(maxLength)

def printTable(table):
    colWidths = [0] * len(table)
    print(colWidths)
    # print(colWidth)
    lengthOfLists = len(table[0])
    # print(lengthOfLists)
    for tableLen in range(len(table)):
        sortedTable = sorted(table[tableLen], key=len)
        colWidths[tableLen] = len(sortedTable[-1])  
        print(colWidths)
        print(tableLen)
    for stringIndex in range(lengthOfLists):
        
        for listIndex in range(len(table)):
            string = table[listIndex][stringIndex]
            print(string.rjust(colWidths[listIndex]), end=' ')
        print()
printTable(tableData)



