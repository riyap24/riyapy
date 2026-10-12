arr = [1,2,2,2,3,4]
key = 2

for i in range (len(arr)):
    if arr[i]==key:
        print("first occurence",i)
        break
    else:
        print("not found")