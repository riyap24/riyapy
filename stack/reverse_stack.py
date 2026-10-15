text = input("Enter a string: ")
stack= list(text)
result=""

while stack:
    result += stack.pop()
    
print("Reversed string:",result)

print(result)