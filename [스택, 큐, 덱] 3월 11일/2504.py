brackets = input()
temp = 1
answer = 0
    
stack = []
for i in range(len(brackets)):
    if brackets[i] == '(':
        stack.append('(')
        temp *= 2
    elif brackets[i] == ')':
        if not stack or stack[-1] == '[':
           print(0)
           exit(0)
        elif brackets[i-1] == '(':
            answer += temp
        temp //= 2
        stack.pop()
    elif brackets[i] == '[':
            temp *= 3
            stack.append('[')
    else:
        if not stack or stack[-1] == '(':
            print(0)
            exit(0)
        elif brackets[i-1] == '[':
            answer += temp
        temp //= 3
        stack.pop()
if stack:
    print(0)
    exit(0)
print(answer)