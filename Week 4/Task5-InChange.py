def inChange(n):
  if n <= 0:
    return 1
  Previous = inChange(n-1)
  Previous2 = inChange(n-2)
  return Previous + (Previous - Previous2) + 1

print(inChange(5))
#recursive function = calling out its own function inside the function
