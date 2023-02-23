def factorial(n):
  facList = []
  if n == 1:
    return [1]
  else:
    facList += factorial(n-1)
    facList.append(facList[-1] * n)
  return facList

n = int(input("Enter input: "))
print(factorial(n))
#recursive function that takes input positive integer N then returns list L of factoral values with length N
#recursive function = calling out its own function inside the function
