arr=[10,20,30,40,50]
key = int(input("Enter element:"))
low,high = 0,len(arr)

while low< high:
    mid = (low+high)//2
    
    if arr[mid]== key:
        low = mid +1
    else:
        high = mid
print("insertion position:", low)