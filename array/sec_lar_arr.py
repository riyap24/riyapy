arr = [10,25,5,40,15]
unique = list(set(arr))
unique.sort()

if len(unique) >=2:
    print("second largest:", unique[-2])
    
else:
    print("No second largest element")