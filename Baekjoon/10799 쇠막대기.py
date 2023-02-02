n = list(input())

stack = []
result = 0
for a,b in zip(n,n[1:]+['']) :
    if stack and a=="(" and b ==")" :
        result += len(stack)
    elif a == "(" and b =="(" :
        stack.append(a)
    elif a == ")" and b == ")" :
        stack.pop()
        result += 1

print(result)