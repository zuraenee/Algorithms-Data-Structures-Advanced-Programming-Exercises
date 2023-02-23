def numbers(list):
  num = list.pop()
  if num == 1:
    return 1
  return num + numbers(list)

print(numbers([1, 2, 3, 4, 5, 6]))

#recursive function = calling out its own function inside the function
