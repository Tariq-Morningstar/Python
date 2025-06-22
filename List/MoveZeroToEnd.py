"""
    Complexity:
        Time: O(n)
        Space: O(n)
"""

def MoveZerotoEnd(arr):
    for i in arr:
        if i!=0:
            arr1.append(i)
        else:
            arr2.append(i)
    return arr1 + arr2

arr=[1,2,0,4]
arr1=[]
arr2=[]
print(MoveZerotoEnd(arr))
