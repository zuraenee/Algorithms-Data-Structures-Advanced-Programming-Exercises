Stack = [2,17,12,5,66,20,7]
Min = Stack[0]
while len(Stack) != 0:
  Item = Stack.pop()
  if Item > Min:
    Min = Item
print(Min)
