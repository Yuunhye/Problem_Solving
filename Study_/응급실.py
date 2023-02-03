from collections import deque

N, M = map(int, input().split())
risk = deque([int(x) for x in input().split()]) #위험도
n = deque([int(i) for i in range(N)])   #환자의 초기 순서

while(1) :
    if M not in n : #M번째 환자가 존재하지 않으면 break (진료를 받은 것이므로)
        break
    temp = risk.popleft()
    if temp >= max(risk) :  #환자가 진료를 받을 수 있는 경우
        n.popleft()
    else :      #더 큰 위험도를 가진 환자가 대기목록에 있어서 진료를 받지 못하는 경우
        risk.append(temp)
        n.append(n.popleft())

print(N-len(n))


#다른 사람 풀이
"""
from collections import deque

n, m=map(int, input().split())
Q=[(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
Q=deque(Q)
cnt=0
while True:
    cur=Q.popleft()
    if any(cur[1]<x[1] for x in Q):
        Q.append(cur)
    else:
        cnt+=1
        if cur[0]==m:
            print(cnt)
            break
"""