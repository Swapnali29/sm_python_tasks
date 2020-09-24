# Task 9

# Please write a binary search function which searches an item in a sorted list.
# The function should return the index of element to be searched in the list.

aList = [1,3,5,6,8,9,10,12,34,56,78,456]
def BinarySearch(aList, target, start, end):
    #aList = sorted(aList)

    if end-start+1 <= 0:
        return False
    else:
        midpoint = start + (end - start) // 2
        if aList[midpoint] == target:
            return midpoint
        else:
            if target < aList[midpoint]:
                return BinarySearch(aList, target, start, midpoint-1)
            else:
                return BinarySearch(aList ,target, midpoint+1, end)

print(BinarySearch(aList,12, 0, len(aList)))