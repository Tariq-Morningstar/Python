def AdjacentSum(arr,target):
    for i in range(len(arr)-1):
        if arr[i] + arr[i+1] == target:
            return arr[i],arr[i+1]
    return 0
arr = [1,3,2,5]
target = 7
print(AdjacentSum(arr,target))
