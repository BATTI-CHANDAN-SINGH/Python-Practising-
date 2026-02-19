#The weight of watermelon should divide in to two parts it not might be equal but both should be even.
#example: 8 -> [[4,4], [2,6]] or [3,5] (3,5 is not valid as 5 is odd)

Weight = int(input("Enter the weight of watermelon: "))
arr=[]
for i in range(1, Weight+1):
    if i%2==0 and (Weight-i)%2==0:
        arr.append([i, Weight-i])
if arr is True:
    print(arr)
else:
    print("No even distribution possible ")
