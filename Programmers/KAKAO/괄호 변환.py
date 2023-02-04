def solution(p):
    answer = ''
    if p.strip() == "" :
        return answer
    
    u, v = '', ''
    op, cl = 0, 0
    for i in range(len(p)):
        if p[i] == "(" :
            op += 1
        else :    #p[i] == ")"
            cl += 1
        u += p[i]
        if op == cl :
            v = p[i+1:]
            break
            
    #u가 올바른 괄호 문자열인지 판단
    stack = []
    check = False
    if u[0] == "(" :
        for j in u :
            if stack and j==")" and stack[-1] == "(" :
                stack.pop()
            else :
                stack.append(j)
        if not(stack) : #stack에 원소가 남아있지 않으면 올바른 괄호 문자열이다.
            check = True

    if check :
        answer += u
        answer += solution(v)
    else :
        answer += "("
        answer += solution(v)
        answer += ")"
        u = list(map(lambda x : "(" if x==")" else ")",u[1:len(u)-1]))
        answer += ''.join(u)
    return answer

#다른 사람 풀이
"""
def solution(p):
    if p=='': return p
    r=True; c=0
    for i in range(len(p)):
        if p[i]=='(': c-=1
        else: c+=1
        if c>0: r=False
        if c==0:
            if r:
                return p[:i+1]+solution(p[i+1:])
            else:
                return '('+solution(p[i+1:])+')'+''.join(list(map(lambda x:'(' if x==')' else ')',p[1:i]) ))
"""