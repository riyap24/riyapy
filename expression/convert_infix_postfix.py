def infix_to_postfix(expression):
    stack = []
    result = []
    priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    
    for ch in expression:
        if ch.isalnum():
            result.append(ch)
        elif ch == '(':
            stack.append(ch)
        elif ch == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            if stack:
                stack.pop()  
            # Pop operators with higher or equal priority
            while stack and stack[-1] != '(' and priority.get(ch, 0) <= priority.get(stack[-1], 0):
                result.append(stack.pop())
            stack.append(ch)
            
    while stack:
        result.append(stack.pop())
        
    return ''.join(result)



print(infix_to_postfix("a*(b+c)"))