from collections import deque
def solution(number, k):
    num = deque(number)
    stack = list()
    while (k>0 and num) :
        n = num.popleft()
        while (stack and k>0 and stack[-1]<n) :
            stack.pop()
            k -= 1
        stack.append(n)
    
    if k!=0 :   #num이 남아있지 않음
        stack = stack[:-k]   #뒤에서 k개만큼 제거
    else :
        stack += num
    answer = ''.join(stack)
    return answer