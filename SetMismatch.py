
def SetMismatch(arr):
    empty_list=[]
    freq={}
    for ky in arr:
        freq[ky]=freq.get(ky,0)+1

        if freq[ky]>1:
            empty_list.append(ky)
    for nums in range(min(arr),max(arr)+1):
        if nums not in freq:
            empty_list.append(nums)
    return empty_list 

print(SetMismatch([1,2,2,4]))
