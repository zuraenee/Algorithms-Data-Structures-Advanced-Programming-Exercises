def reverseMergeSortList(list1, list2):
    list1 = list1[::-1]
    list2 = list2[::-1]
    list1.extend(list2)
    list1.sort(reverse=True)
    return list1

print(reverseMergeSortList([1,2,3], [4,5,6]))
print(reverseMergeSortList([1,7,3], [9,2,4]))
