from collections import deque
N, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
S,X,Y = map(int, input().split())
virus = list()
for i in range(N) :
    for j in range(N) :
        if graph[i][j] != 0 :
            virus.append((graph[i][j], i, j,0))   #바이러스 번호, 위치, 시간 정보 저장
virus.sort()    #바이러스 번호순으로(오름차순) 정렬이 되기 때문에 낮은 번호의 바이러스가 먼저 증식할 수 있다.
virus = deque(virus)
dx = [1,-1,0,0]
dy = [0,0,1,-1]

#bfs
while virus :
    v,x,y,t = virus.popleft()   #바이러스 번호, 위치(x,y), 시간
    if t==S :
        break
    for i in range(4) :
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<N and 0<=ny<N and graph[nx][ny] == 0 :   #해당 위치에 바이스러가 존재하지 않으면 증식 가능
            graph[nx][ny] = v
            virus.append((v,nx,ny,t+1))

print(graph[X-1][Y-1])