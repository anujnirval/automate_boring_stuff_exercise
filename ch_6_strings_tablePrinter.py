tableData = [['apples','oranges','cherries','banana'],['Alice','Bob','Carol','David'],['dogs','cats','moose','goose']]

def printTable(data):
    colWidths = [0] * len(data)
    
    for i in range(len(data)):
        item_length=[]
        for item in data[i]:
            item_length.append(len(item))
            item_length.sort()
            colWidths[i]=item_length[-1]
    for x in range(len(data[0])):
        for y in range(len(data)):
            print(str(data[y][x].rjust(colWidths[y])),end=" ")
        print()

printTable(tableData)
