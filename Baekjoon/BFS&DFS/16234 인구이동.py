import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N,L,R = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]

dx = [1,-1,0,0]  #상하좌우
dy = [0,0,1,-1]
open_set = set()
visited = [[False] * N for _ in range(N)]
ans = 0

#연합을 구하는 함수
def dfs(x,y) :
    global L, R
    visited[x][y] = True
    for i in range(4) :
        nx = x+dx[i]
        ny = y+dy[i]
		
        if nx<0 or ny<0 or nx>=N or ny>=N or visited[nx][ny] :
            continue
        if L<=abs(A[nx][ny] - A[x][y])<=R :
            open_set.add((nx,ny))
            dfs(nx,ny)

#방문하지 않은 모든 좌표에 대해서 dfs를 수행하도록 하고, dfs를 통해 만들어진 연합들을 반환하는 함수
def move() :
    global open_set
    unity = list()  #연합들을 저장할 리스트
    for i in range(N) :
        for j in range(N) :
            if visited[i][j] == False :
                open_set = {(i,j)}
                dfs(i,j)
                if len(open_set)>1 :  #연합이 존재하면 연합을 리스트에 추가한다.
                    unity.append(open_set)
    
    return unity

#연합이 더이상 존재하지 않을 때까지 인구이동 수행
while (1) :
    res = move()
    if res :
        ans += 1
        for u in res :
            count = 0
            for (x,y) in u :
                count+= A[x][y]
            num = count//len(u)
            for (x,y) in u :
                A[x][y] = count//len(u)
        visited = [[False] * N for _ in range(N)]  #방문 정보 초기화
    else :
        break

print(ans)