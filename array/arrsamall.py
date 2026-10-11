#Find the smallest element in a list

arr = [10 ,25,5,40,15]
smallest = arr[0]

for i in arr:
    if i < smallest:
        smallest = i

print("Smallest:", smallest)
