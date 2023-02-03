from collections import deque
N, K = map(int, input().split())
queue = deque([int(i) for i in range(1,N+1)])

while len(queue) != 1 :
    for j in range(K-1) :
        queue.append(queue.popleft())
    queue.popleft()
print(queue[0])


#queue 이용 X
"""
N, K = map(int, input().split())
princes = [int(i) for i in range(1,N+1)]
start = 0
while len(princes) != 1 :
    index = (start + (K-1))%len(princes)
    del princes[index]
    start = index

print(princes[0])
"""