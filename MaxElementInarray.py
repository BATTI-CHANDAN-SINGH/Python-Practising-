def maxelementinarry(arr):
    max_value=arr[0]
    for num in range(len(arr)):
        if arr[num] > max_value:
            max_value = arr[num]
    return num+1
arr=list(map(int,input("Enter the elements of the array: ").split()))
print("The maximum element in the array is: ",maxelementinarry(arr))

