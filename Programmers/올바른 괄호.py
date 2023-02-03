def solution(s):
    if s[0] == ")" :  #special case
        return False
    
    stack = []
    for i in s :
        if i == "(" :
            stack.append(i)
        elif stack and stack[-1] == "(" :
            stack.pop()
    if stack :   #stack에 "("가 남아있으면 짝이 맞지 않는다는 말이므로 False
        return False
    else :       #stack이 다 비워졌으면 True
        return True