def UniqueElement(arr,freq):
    for i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    
    unique_Element = []
    for key in freq:
        if freq[key] == 1:
            unique_Element.append(key)
            
    return unique_Element

arr = [1,2,3,4,3,4,1]
freq = {}
print(UniqueElement(arr,freq))
