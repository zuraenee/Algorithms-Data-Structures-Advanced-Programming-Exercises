def deleteAllNodes(self):
    if self.isEmpty() is False:
        self.head = None
        print("All items are deleted successfully")
    else:
        print("Linked List is empty, Delete Failed")
