def deleteAt(self, position):
    if self.head is None:
        return self.head
    else:
        currentNode = self.head
        currentPosition = 0
        while True:
            if currentPosition == position:
                prevNode.next = currentNode.next
                currentNode.next = None
                break
            prevNode = currentNode
            currentNode = currentNode.next
            currentPosition += 1
        return self.head
