import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    day = deque()
    for p, s in zip(progresses, speeds) :   #작업기간
        day.append(math.ceil((100-p)/s))
    
    while day :
        cur = day[0]
        count = 0
        while day and (cur >= day[0]) : #작업기간이 앞에 배포되는 기능보다 짧은 경우 같이 배포됨
            day.popleft()
            count += 1
        answer.append(count)
        
    return answer