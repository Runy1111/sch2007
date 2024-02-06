a = input()
stack = []
for i in a:
    if i == '(':
        stack.append('(')
    elif i == '[':
        stack.append('[')
    elif i == '{':
        stack.append('{')
    elif i == ')':
        if len(stack) == 0:
            stack.append(1)
            break
        elif stack[-1] != '(':
            break
        else:
            stack.pop()
    elif i == ']':
        if len(stack) == 0:
            stack.append(1)
            break
        elif stack[-1] != '[':
            break
        else:
            stack.pop()
    elif i == '}':
        if len(stack) == 0:
            stack.append(1)
            break
        elif stack[-1] != '{':
            break
        else:
            stack.pop()

if len(stack) == 0:
    print('YES')
else:
    print('NO')
