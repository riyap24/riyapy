arr = [2, 7, 11, 15]
target = 9

seen = {}

for i, num in enumerate(arr):
    difference = target - num

    if difference in seen:
        print("Indices:", seen[difference], i)
        break

    seen[num] = i