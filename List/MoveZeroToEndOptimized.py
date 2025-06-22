def MoveZerotoEnd(arr,pos):
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[pos] = arr[i]
            pos+=1
            
    for i in range(pos, len(arr)):
        arr[i]=0
    return arr
        
pos=0
arr=[1,2,0,4]

print(MoveZerotoEnd(arr,pos))


