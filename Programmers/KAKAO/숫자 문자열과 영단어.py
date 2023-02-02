def solution(s):
    answer = 0   
    if (s.isnumeric()) :    #s가 숫자로만 이루어진 경우
        answer = int(s)
        return answer
    
    num = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    i = 0
    for n in num :
        if n in s :
            s = s.replace(n,str(i))
        i += 1
    answer = int(s)
    return answer