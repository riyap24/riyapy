arr =[10,20,30,40,50]
k = int(input("Enter rotations:"))

k %= len(arr)
if k:
    arr = arr[-k:] + arr[:-k]
    
print(arr)