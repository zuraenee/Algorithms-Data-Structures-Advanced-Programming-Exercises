def printToN(n):
    if n == 1:
        print(1)
        return
    printToN(n - 1)
    print(n)


printToN(3)
#recursive function = calling out its own function inside the function

def printSquare(n):
    if n == 1:
        print(1)
        return
    printSquare(n - 1)
    print(n * n)


printSquare(5)
#recursive function = calling out its own function inside the function

def sumOfSquares(n):
    if n == 1:
        return 1
    return (n * n) + sumOfSquares(n - 1)

print(sumOfSquares(5))
#recursive function = calling out its own function inside the function
