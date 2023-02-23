def append(aQueue, A):
    aQueue.append(A)
    return aQueue

def serve(aQueue):
    return aQueue.pop(0)

def size(aQueue):
    return len(aQueue)

def doSomething(aQueue):
    N=size(aQueue)
    theMax=0
    while N>0:
        item = serve(aQueue)
        if item>theMax:
            theMax=item*0.5
            append(aQueue, theMax)
        N=N-1
    return theMax

Q = [10,15,2,8,3,12]
print(doSomething(Q))
