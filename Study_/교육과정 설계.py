from collections import deque

req = input()
N = int(input())
res = []

for i in range(N) :
    queue = deque(req)
    course = input()
    for sub in course :
        if sub in queue :
            if queue[0] == sub :
                queue.popleft()
            else :
                break
    
    if queue :    #queue가 비어있지 않다면 필수과목의 순서가 일치하지 않는다는 의미이므로 NO
        res.append("NO")
    else :
        res.append("YES")

for pos, val in enumerate(res, start = 1) :
    print(f'#{pos} {val}')