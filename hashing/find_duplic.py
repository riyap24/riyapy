arr = [1, 2, 3, 2, 4, 5, 1]

seen = set()

for num in arr:
    if num in seen:
        print("Duplicate:", num)
    else:
        seen.add(num)