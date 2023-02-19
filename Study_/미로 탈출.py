from collections import deque

N, M = map(int,input().split())
graph = [list(map(int, input())) for i in range(N)]
can_visit = []
for a in graph :  #0 : False, 1 : True
    can_visit.append(list(map(bool, a)))

#bfs
queue = deque([(0,0)])
can_visit[0][0] = False
dx = [-1,0,1,0]
dy = [0,1,0,-1]
while queue :
    y, x = queue.popleft()  #행, 열
    for i in range(4) :
        ny = y+dy[i]
        nx = x+dx[i]
        if ny<0 or nx<0 or ny>=N or nx>=M :
            continue
        if can_visit[ny][nx] :  #방문할 수 있으면 (이전에 방문한 적이 없거나 벽이 아님)
            can_visit[ny][nx] = False  #방문 처리
            queue.append((ny,nx))  
            graph[ny][nx] = graph[y][x] + 1 

print(graph[N-1][M-1])

#풀이
"""
from collections import deque

def bfs(x,y) :
    queue = deque()
    queue.append((x,y))

    while queue :
        x,y = queue.popleft()
        #현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
          
            #미로 찾기 공간을 벗어난 경우 무시
            if nx<0 or nx>=N or ny<0 or ny>=M :
                continue
            #벽인 경우 무시
            if graph[nx][ny] == 0 :
                continue
            #해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1 :
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    #가장 오른쪽 아래까지의 최단 거리 반환
    return graph[N-1][M-1]

N, M = map(int, input().split())
graph = [list(map(int, input())) for i in range(N)]

#이동할 네 가지 방향 정의 (상, 하, 좌, 우)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

#bfs를 수행한 결과 출력
print(bfs(0,0))
"""