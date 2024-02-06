a = list(map(str, input().split()))
stack = []
for i in a:
    if i == '-':
        stack.append(-stack.pop() + stack.pop())
    elif i == '+':
        stack.append(stack.pop() + stack.pop())
    elif i == '*':
        stack.append(stack.pop() * stack.pop())
    else:
        stack.append(int(i))
print(stack.pop())
