def duplicate(list1, list2):
  outputList = []
  for item in list1:
    if item in list2:
      outputList.append(item)
  return outputList

print(duplicate([2,17,12,5,66,20,7], [2,12,66]))
