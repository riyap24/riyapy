#Find the largest element in a list

arr = [10 ,25,5,40,15]
largest = arr[0]

for i in arr:
    if i > largest:
        largest = i
        
print("Largest:", largest)
