def addAllItems(self):
    currentNode = self.head
    while currentNode is not None:
        self.count += currentNode.data
        currentNode = currentNode.next
    return self.count
