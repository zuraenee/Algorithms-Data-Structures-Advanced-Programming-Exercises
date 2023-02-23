def getMinIndex(myList, start, stop, distOrPrice):
    min_index = start
    for i in range(start + 1, stop):
        dataPairs = myList[i]
        minList = myList[min_index]
        if float(dataPairs[distOrPrice]) < float(minList[distOrPrice]):
            min_index = i
    return min_index


def selectionSortDistance(list):
    n = len(list)
    for index in range(n):
        min_position = getMinIndex(list, index, n, 0)
        temp = list[index]
        list[index] = list[min_position]
        list[min_position] = temp


def selectionSortPrice(list):
    n = len(list)
    for index in range(n):
        min_position = getMinIndex(list, index, n, 1)
        temp = list[index]
        list[index] = list[min_position]
        list[min_position] = temp


def printList(list):
    for line in list:
        print(line[0], "Miles, $", line[1])



fileName = input("Enter file name, with .txt")
file = open(fileName)
list = []
for line in file:
    line = line.strip().split(",")
    list.append(line)

choice = int(input("Enter choice : (1)Print - (2)Sort on Distance - (3)Sort on Price - (4)Quit : "))
if (choice==1):
    printList()
elif (choice==2):
    print("\nFile sorted by distance")
    selectionSortDistance(list)
    printList(list)
elif (choice==3):
    print("\nFile sorted by price")
    selectionSortPrice(list)
    printList(list)
else:
    print("quitting")


