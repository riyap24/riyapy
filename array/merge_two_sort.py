a = [ 10, 30, 50]
b = [20, 40, 60]
result = []
i = j = 0

while i < len(a) and j < len(b):
    if a[i] <=b[j]:
        result.append(a[i])
        i+= 1
    else:
        result.append(b[j])
        j+= 1
        
result.extend(a[i:])
result.extend(b[j:])

print(result)