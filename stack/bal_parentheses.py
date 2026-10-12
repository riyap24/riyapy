exp = input("Enter exp")
stack=[]
pairs={")": "(", "}": "{", "]": "["}
balanced = True
for i in exp:
    for ch in exp:
        if ch in "([{":
            stack.append(ch)
        elif ch in ")]}":
            if not stack or stack.pop !=pairs[ch]:
                balanced = False
                break
            
if stack:
    balanced = False
    
print("balanced" if balanced else "not balanced")