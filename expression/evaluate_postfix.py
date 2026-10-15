#Enter operands separated by spaces, for example 5 3 + 2 *.

import token


exp = input("Enter a postfix expression:")
stack = []

for token in exp():
    if token.lstrip().isdigit():
        stack.append(int(token))
    else:
        b = stack.pop()
        a = stack.pop() 
        
    if token =='+':
        stack.append(a + b)
    elif token == '-':
        stack.append(a - b)         
    elif token =='*':
        stack.append(a*b)
    elif token =='/':
        stack.append(int(a/b))
        
print("Result:", stack[-1])