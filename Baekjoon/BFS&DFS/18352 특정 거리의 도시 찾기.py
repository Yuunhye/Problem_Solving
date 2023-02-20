import sys
input = sys.stdin.readline  #이거 없으면 시간초과 남
from collections import deque

N, M, K, X = map(int, input().split())
graph = [[] for i in range(N+1)]  #각 도시에서 도달할 수 있는 도시의 정보를 저장
for i in range(M) :
    a, b = map(int, input().split())
    graph[a].append(b)

d = [-1] * (N+1)    #출발 도시로부터 각 도시까지의 최단 거리를 저장
d[X] = 0            #자기 자신으로 가는 최단 거리는 0
queue = deque([X])

#bfs
while queue :
    v = queue.popleft()

    for i in graph[v] :
        if d[i] == -1 : #이전에 방문한 적이 없는 경우 (첫 방문인 경우)
            queue.append(i)
            d[i] = d[v] + 1  #최단 거리 갱신

if K in d :
    for i in range(1,N+1) :
        if d[i] == K :
            print(i)
else :
    print(-1)