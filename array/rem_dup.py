arr =[10, 20, 30 ,20, 40]
result =[]

for x in arr:
    if x not in result:
        result.append(x)
        
print(result)