def numberOfNodes(self):
    currentNode = self.head
    while currentNode is not None:
        self.count += 1
        currentNode = currentNode.next
    return self.count
