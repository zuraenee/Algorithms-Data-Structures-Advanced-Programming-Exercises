def minSort(list):
    resultList=[]
    print("Original list", list)
    while len(list)>0: #this is so that the loop will stop when the list is empty
        for i in list:
            if i==min(list):
                resultList.append(i)
                list.remove(i)
    print("Final list", resultList)


minSort([4,1,5,2])
