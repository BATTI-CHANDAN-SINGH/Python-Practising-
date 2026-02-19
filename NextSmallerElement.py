arr = list(map(int,input("enter the values with comma:").split(',')))
n = len(arr)
a = []

for i in range(n):
    nearest_val = None
    nearest_dist = 0
    
    for j in range(i+1, n):
        if arr[j] < arr[i]:
            diff = abs(arr[i] - arr[j])
            
            if nearest_val is None or diff < nearest_val:
                nearest_val = diff
                nearest_dist = j - i
                
    a.append(nearest_dist)

print(a)

