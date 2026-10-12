arr=[ 1,2,2,3,1,2,4]
frequency ={}

for x in arr:
    frequency[x] = frequency.get(x,0) + 1
    
print(frequency)