def deleteNegativeNode(self):
    currentNode = self.head
    while currentNode is not None:
        if currentNode.data < 0:
            self.deleteAt(currentNode.data)
        currentNode = currentNode.next
