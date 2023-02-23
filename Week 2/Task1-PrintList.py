def printList(list):
    for line in list:
        print(line[0], "Miles, $", line[1])


fileName = str(input("Enter file name, with .txt : "))
file = open(fileName)
list = []
for line in file:
    line = line.strip().split(",")
    list.append(line)
print(list)
print()
printList(list)
