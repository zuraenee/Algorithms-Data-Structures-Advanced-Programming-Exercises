def smallestItem(list): # Could us min to simplify but I'm not sure if it counts as recursion
  if len(list) == 1:
    return list[0]
  num = list.pop()
  other = smallestItem(list)
  if num < other:
    return num
  else:
    return other

print(smallestItem([3, 2, 5, 6]))
#recursive function = calling out its own function inside the function
